from django.db.models import Q
from .models import Course, Lesson, Material, Enrollment

class CourseService:
    @staticmethod
    def create_course(author, title, description, difficulty='beginner', thumbnail=None):
        course = Course.objects.create(
            author=author,
            title=title,
            description=description,
            difficulty=difficulty,
            thumbnail=thumbnail
        )
        return course
    
    @staticmethod
    def update_course(course, **kwargs):
        for key, value in kwargs.items():
            if hasattr(course, key):
                setattr(course, key, value)
        course.save()
        return course
    
    @staticmethod
    def delete_course(course):
        course.delete()
    
    @staticmethod
    def get_published_courses():
        return Course.objects.filter(is_published=True)
    
    @staticmethod
    def get_author_courses(author):
        return Course.objects.filter(author=author)
    
    @staticmethod
    def search_courses(query):
        return Course.objects.filter(
            Q(title__icontains=query) | Q(description__icontains=query),
            is_published=True
        )

class LessonService:
    @staticmethod
    def create_lesson(course, title, content, order=0):
        lesson = Lesson.objects.create(
            course=course,
            title=title,
            content=content,
            order=order
        )
        return lesson
    
    @staticmethod
    def update_lesson(lesson, **kwargs):
        for key, value in kwargs.items():
            if hasattr(lesson, key):
                setattr(lesson, key, value)
        lesson.save()
        return lesson
    
    @staticmethod
    def delete_lesson(lesson):
        lesson.delete()
    
    @staticmethod
    def get_course_lessons(course):
        return Lesson.objects.filter(course=course)

class MaterialService:
    @staticmethod
    def create_material(lesson, title, file, material_type='document', description=''):
        material = Material.objects.create(
            lesson=lesson,
            title=title,
            file=file,
            material_type=material_type,
            description=description
        )
        return material
    
    @staticmethod
    def delete_material(material):
        material.file.delete()
        material.delete()
    
    @staticmethod
    def get_lesson_materials(lesson):
        return Material.objects.filter(lesson=lesson)

class EnrollmentService:
    @staticmethod
    def enroll_user(user, course):
        enrollment, created = Enrollment.objects.get_or_create(user=user, course=course)
        return enrollment
    
    @staticmethod
    def unenroll_user(user, course):
        Enrollment.objects.filter(user=user, course=course).delete()
    
    @staticmethod
    def is_enrolled(user, course):
        return Enrollment.objects.filter(user=user, course=course).exists()
    
    @staticmethod
    def get_user_enrollments(user):
        return Enrollment.objects.filter(user=user).select_related('course')
