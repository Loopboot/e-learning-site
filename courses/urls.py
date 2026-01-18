from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('courses/', views.course_list, name='course_list'),
    path('courses/<slug:slug>/', views.course_detail, name='course_detail'),
    path('courses/<slug:slug>/enroll/', views.enroll_course, name='enroll_course'),
    path('courses/<slug:slug>/lessons/<int:lesson_id>/', views.lesson_detail, name='lesson_detail'),
    path('my-courses/', views.my_courses, name='my_courses'),
    
    # Author dashboard
    path('author/dashboard/', views.author_dashboard, name='author_dashboard'),
    path('author/courses/create/', views.create_course, name='create_course'),
    path('author/courses/<slug:slug>/edit/', views.edit_course, name='edit_course'),
    path('author/courses/<slug:slug>/delete/', views.delete_course, name='delete_course'),
    
    # Lesson management
    path('author/courses/<slug:slug>/lessons/', views.manage_lessons, name='manage_lessons'),
    path('author/courses/<slug:slug>/lessons/create/', views.create_lesson, name='create_lesson'),
    path('author/courses/<slug:slug>/lessons/<int:lesson_id>/edit/', views.edit_lesson, name='edit_lesson'),
    path('author/courses/<slug:slug>/lessons/<int:lesson_id>/delete/', views.delete_lesson, name='delete_lesson'),
    
    # Material management
    path('author/courses/<slug:slug>/lessons/<int:lesson_id>/materials/', views.manage_materials, name='manage_materials'),
    path('author/courses/<slug:slug>/lessons/<int:lesson_id>/materials/create/', views.create_material, name='create_material'),
    path('author/courses/<slug:slug>/lessons/<int:lesson_id>/materials/<int:material_id>/delete/', views.delete_material, name='delete_material'),
    path('materials/<int:material_id>/download/', views.download_material, name='download_material'),
]
