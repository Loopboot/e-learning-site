from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import FileResponse, Http404
from .models import Course, Lesson, Material
from .forms import CourseForm, LessonForm, MaterialForm
from .services import CourseService, LessonService, MaterialService, EnrollmentService

def home(request):
    courses = CourseService.get_published_courses()
    return render(request, 'courses/home.html', {'courses': courses})

def course_list(request):
    query = request.GET.get('q', '')
    if query:
        courses = CourseService.search_courses(query)
    else:
        courses = CourseService.get_published_courses()
    return render(request, 'courses/course_list.html', {'courses': courses, 'query': query})

def course_detail(request, slug):
    course = get_object_or_404(Course, slug=slug, is_published=True)
    lessons = LessonService.get_course_lessons(course)
    is_enrolled = False
    if request.user.is_authenticated:
        is_enrolled = EnrollmentService.is_enrolled(request.user, course)
    return render(request, 'courses/course_detail.html', {
        'course': course,
        'lessons': lessons,
        'is_enrolled': is_enrolled
    })

def lesson_detail(request, slug, lesson_id):
    course = get_object_or_404(Course, slug=slug, is_published=True)
    lesson = get_object_or_404(Lesson, id=lesson_id, course=course)
    
    if request.user.is_authenticated:
        is_enrolled = EnrollmentService.is_enrolled(request.user, course)
        is_author = course.author == request.user
        if not (is_enrolled or is_author):
            messages.error(request, 'You must enroll in this course to view lessons.')
            return redirect('course_detail', slug=slug)
    else:
        messages.error(request, 'Please log in to view lessons.')
        return redirect('login')
    
    materials = MaterialService.get_lesson_materials(lesson)
    return render(request, 'courses/lesson_detail.html', {
        'course': course,
        'lesson': lesson,
        'materials': materials
    })

@login_required
def enroll_course(request, slug):
    course = get_object_or_404(Course, slug=slug, is_published=True)
    EnrollmentService.enroll_user(request.user, course)
    messages.success(request, f'Successfully enrolled in {course.title}!')
    return redirect('course_detail', slug=slug)

@login_required
def my_courses(request):
    enrollments = EnrollmentService.get_user_enrollments(request.user)
    return render(request, 'courses/my_courses.html', {'enrollments': enrollments})

@login_required
def author_dashboard(request):
    if request.user.role != 'author':
        messages.error(request, 'You must be an author to access this page.')
        return redirect('home')
    
    courses = CourseService.get_author_courses(request.user)
    return render(request, 'courses/author_dashboard.html', {'courses': courses})

@login_required
def create_course(request):
    if request.user.role != 'author':
        messages.error(request, 'You must be an author to create courses.')
        return redirect('home')
    
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES)
        if form.is_valid():
            course = CourseService.create_course(
                author=request.user,
                title=form.cleaned_data['title'],
                description=form.cleaned_data['description'],
                difficulty=form.cleaned_data['difficulty'],
                thumbnail=form.cleaned_data.get('thumbnail')
            )
            course.is_published = form.cleaned_data['is_published']
            course.save()
            messages.success(request, 'Course created successfully!')
            return redirect('author_dashboard')
    else:
        form = CourseForm()
    return render(request, 'courses/course_form.html', {'form': form, 'action': 'Create'})

@login_required
def edit_course(request, slug):
    course = get_object_or_404(Course, slug=slug, author=request.user)
    
    if request.method == 'POST':
        form = CourseForm(request.POST, request.FILES, instance=course)
        if form.is_valid():
            form.save()
            messages.success(request, 'Course updated successfully!')
            return redirect('author_dashboard')
    else:
        form = CourseForm(instance=course)
    return render(request, 'courses/course_form.html', {'form': form, 'action': 'Edit', 'course': course})

@login_required
def delete_course(request, slug):
    course = get_object_or_404(Course, slug=slug, author=request.user)
    if request.method == 'POST':
        CourseService.delete_course(course)
        messages.success(request, 'Course deleted successfully!')
        return redirect('author_dashboard')
    return render(request, 'courses/course_confirm_delete.html', {'course': course})

@login_required
def manage_lessons(request, slug):
    course = get_object_or_404(Course, slug=slug, author=request.user)
    lessons = LessonService.get_course_lessons(course)
    return render(request, 'courses/manage_lessons.html', {'course': course, 'lessons': lessons})

@login_required
def create_lesson(request, slug):
    course = get_object_or_404(Course, slug=slug, author=request.user)
    
    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            LessonService.create_lesson(
                course=course,
                title=form.cleaned_data['title'],
                content=form.cleaned_data['content'],
                order=form.cleaned_data['order']
            )
            messages.success(request, 'Lesson created successfully!')
            return redirect('manage_lessons', slug=slug)
    else:
        form = LessonForm()
    return render(request, 'courses/lesson_form.html', {'form': form, 'course': course, 'action': 'Create'})

@login_required
def edit_lesson(request, slug, lesson_id):
    course = get_object_or_404(Course, slug=slug, author=request.user)
    lesson = get_object_or_404(Lesson, id=lesson_id, course=course)
    
    if request.method == 'POST':
        form = LessonForm(request.POST, instance=lesson)
        if form.is_valid():
            form.save()
            messages.success(request, 'Lesson updated successfully!')
            return redirect('manage_lessons', slug=slug)
    else:
        form = LessonForm(instance=lesson)
    return render(request, 'courses/lesson_form.html', {'form': form, 'course': course, 'lesson': lesson, 'action': 'Edit'})

@login_required
def delete_lesson(request, slug, lesson_id):
    course = get_object_or_404(Course, slug=slug, author=request.user)
    lesson = get_object_or_404(Lesson, id=lesson_id, course=course)
    
    if request.method == 'POST':
        LessonService.delete_lesson(lesson)
        messages.success(request, 'Lesson deleted successfully!')
        return redirect('manage_lessons', slug=slug)
    return render(request, 'courses/lesson_confirm_delete.html', {'course': course, 'lesson': lesson})

@login_required
def manage_materials(request, slug, lesson_id):
    course = get_object_or_404(Course, slug=slug, author=request.user)
    lesson = get_object_or_404(Lesson, id=lesson_id, course=course)
    materials = MaterialService.get_lesson_materials(lesson)
    return render(request, 'courses/manage_materials.html', {'course': course, 'lesson': lesson, 'materials': materials})

@login_required
def create_material(request, slug, lesson_id):
    course = get_object_or_404(Course, slug=slug, author=request.user)
    lesson = get_object_or_404(Lesson, id=lesson_id, course=course)
    
    if request.method == 'POST':
        form = MaterialForm(request.POST, request.FILES)
        if form.is_valid():
            MaterialService.create_material(
                lesson=lesson,
                title=form.cleaned_data['title'],
                file=form.cleaned_data['file'],
                material_type=form.cleaned_data['material_type'],
                description=form.cleaned_data['description']
            )
            messages.success(request, 'Material uploaded successfully!')
            return redirect('manage_materials', slug=slug, lesson_id=lesson_id)
    else:
        form = MaterialForm()
    return render(request, 'courses/material_form.html', {'form': form, 'course': course, 'lesson': lesson})

@login_required
def delete_material(request, slug, lesson_id, material_id):
    course = get_object_or_404(Course, slug=slug, author=request.user)
    lesson = get_object_or_404(Lesson, id=lesson_id, course=course)
    material = get_object_or_404(Material, id=material_id, lesson=lesson)
    
    if request.method == 'POST':
        MaterialService.delete_material(material)
        messages.success(request, 'Material deleted successfully!')
        return redirect('manage_materials', slug=slug, lesson_id=lesson_id)
    return render(request, 'courses/material_confirm_delete.html', {'course': course, 'lesson': lesson, 'material': material})

@login_required
def download_material(request, material_id):
    material = get_object_or_404(Material, id=material_id)
    course = material.lesson.course
    
    is_author = course.author == request.user
    is_enrolled = EnrollmentService.is_enrolled(request.user, course)
    
    if not (is_author or is_enrolled):
        raise Http404("You don't have permission to download this material")
    
    try:
        return FileResponse(material.file.open('rb'), as_attachment=True, filename=material.file.name.split('/')[-1])
    except FileNotFoundError:
        raise Http404("File not found")
