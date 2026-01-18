from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from courses.models import Course, Lesson, Material

User = get_user_model()

class Command(BaseCommand):
    help = 'Creates sample data for testing the e-learning platform'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Creating sample data...'))

        # Create sample users
        admin_user = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='admin123',
            role='admin'
        )
        self.stdout.write(self.style.SUCCESS(f'Created admin user: admin/admin123'))

        author1 = User.objects.create_user(
            username='john_doe',
            email='john@example.com',
            password='author123',
            role='author',
            first_name='John',
            last_name='Doe',
            bio='Experienced software developer and educator with 10+ years of experience.'
        )
        self.stdout.write(self.style.SUCCESS(f'Created author: john_doe/author123'))

        author2 = User.objects.create_user(
            username='jane_smith',
            email='jane@example.com',
            password='author123',
            role='author',
            first_name='Jane',
            last_name='Smith',
            bio='Data science expert passionate about teaching machine learning.'
        )
        self.stdout.write(self.style.SUCCESS(f'Created author: jane_smith/author123'))

        student = User.objects.create_user(
            username='student',
            email='student@example.com',
            password='student123',
            role='student',
            first_name='Test',
            last_name='Student'
        )
        self.stdout.write(self.style.SUCCESS(f'Created student: student/student123'))

        # Create sample courses
        course1 = Course.objects.create(
            title='Python Programming for Beginners',
            description='Learn Python programming from scratch. This comprehensive course covers all the basics of Python, including variables, data types, control structures, functions, and object-oriented programming.',
            author=author1,
            difficulty='beginner',
            is_published=True
        )
        
        course2 = Course.objects.create(
            title='Advanced Django Web Development',
            description='Master Django framework and build production-ready web applications. Learn about models, views, templates, authentication, REST APIs, and deployment.',
            author=author1,
            difficulty='advanced',
            is_published=True
        )
        
        course3 = Course.objects.create(
            title='Introduction to Machine Learning',
            description='Dive into the world of machine learning. Learn about supervised and unsupervised learning, neural networks, and practical applications.',
            author=author2,
            difficulty='intermediate',
            is_published=True
        )
        
        course4 = Course.objects.create(
            title='Data Science with Python',
            description='Learn data analysis, visualization, and machine learning with Python. Master pandas, numpy, matplotlib, and scikit-learn.',
            author=author2,
            difficulty='intermediate',
            is_published=False
        )

        self.stdout.write(self.style.SUCCESS('Created 4 sample courses'))

        # Create lessons for course 1
        lesson1_1 = Lesson.objects.create(
            course=course1,
            title='Introduction to Python',
            content='''Welcome to Python Programming!

In this lesson, you'll learn:
- What is Python?
- Why learn Python?
- Setting up your development environment
- Your first Python program

Python is a powerful, versatile programming language that's perfect for beginners and professionals alike. Let's get started!''',
            order=1
        )

        lesson1_2 = Lesson.objects.create(
            course=course1,
            title='Variables and Data Types',
            content='''Understanding Variables and Data Types

Topics covered:
- Variables and naming conventions
- Numeric types (int, float)
- Strings and string operations
- Boolean values
- Type conversion

Variables are containers for storing data. Let's learn how to use them effectively!''',
            order=2
        )

        lesson1_3 = Lesson.objects.create(
            course=course1,
            title='Control Structures',
            content='''Control Flow in Python

Learn about:
- If statements
- Elif and else
- For loops
- While loops
- Break and continue

Control structures allow you to control the flow of your program's execution.''',
            order=3
        )

        # Create lessons for course 2
        lesson2_1 = Lesson.objects.create(
            course=course2,
            title='Django Project Setup',
            content='''Setting Up Your Django Project

What you'll learn:
- Installing Django
- Creating a new project
- Understanding project structure
- Django settings configuration
- Running the development server

Let's set up your first Django project!''',
            order=1
        )

        lesson2_2 = Lesson.objects.create(
            course=course2,
            title='Models and Databases',
            content='''Working with Django Models

Topics:
- Creating models
- Field types
- Migrations
- QuerySets and database queries
- Model relationships

Models are the foundation of your Django application's data layer.''',
            order=2
        )

        # Create lessons for course 3
        lesson3_1 = Lesson.objects.create(
            course=course3,
            title='What is Machine Learning?',
            content='''Introduction to Machine Learning

Overview:
- Definition of machine learning
- Types of machine learning
- Applications in real world
- ML workflow
- Getting started with ML

Machine learning is revolutionizing technology. Let's understand the basics!''',
            order=1
        )

        self.stdout.write(self.style.SUCCESS('Created sample lessons'))

        # Enroll student in courses
        from courses.models import Enrollment
        Enrollment.objects.create(user=student, course=course1)
        Enrollment.objects.create(user=student, course=course3)
        
        self.stdout.write(self.style.SUCCESS('Enrolled student in sample courses'))
        
        self.stdout.write(self.style.SUCCESS('\n================================='))
        self.stdout.write(self.style.SUCCESS('Sample data created successfully!'))
        self.stdout.write(self.style.SUCCESS('================================='))
        self.stdout.write(self.style.SUCCESS('\nLogin credentials:'))
        self.stdout.write(self.style.SUCCESS('Admin: admin/admin123'))
        self.stdout.write(self.style.SUCCESS('Author 1: john_doe/author123'))
        self.stdout.write(self.style.SUCCESS('Author 2: jane_smith/author123'))
        self.stdout.write(self.style.SUCCESS('Student: student/student123'))
