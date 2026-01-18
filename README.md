# E-Learning Platform

A comprehensive e-learning platform built with Django where authors can create and manage courses, and students can enroll and learn.

## Features

### For Students
- Browse and search courses
- Enroll in courses
- View lessons online
- Download course materials
- View author profiles
- Track enrolled courses

### For Authors
- Create and manage courses
- Add lessons to courses
- Upload learning materials (PDFs, videos, documents)
- Publish/unpublish courses
- View course statistics
- Manage only their own content

### For Admins
- Full access to Django admin panel
- Manage all users, courses, lessons, and materials
- Monitor platform activity
- User role management

## Project Structure

```
e-learning-site/
├── courses/              # Course management app
│   ├── models.py        # Course, Lesson, Material, Enrollment models
│   ├── views.py         # All course-related views
│   ├── services.py      # Business logic layer
│   ├── forms.py         # Course, lesson, and material forms
│   ├── admin.py         # Admin panel configuration
│   └── urls.py          # Course URL routing
├── users/               # User management app
│   ├── models.py        # Custom User model
│   ├── views.py         # Authentication and profile views
│   ├── services.py      # User service layer
│   ├── forms.py         # User registration and profile forms
│   ├── admin.py         # User admin configuration
│   └── urls.py          # User URL routing
├── main/                # Main project settings
│   ├── settings.py      # Django settings
│   ├── urls.py          # Root URL configuration
│   └── wsgi.py          # WSGI configuration
├── templates/           # HTML templates
│   ├── base.html        # Base template
│   ├── courses/         # Course templates
│   └── users/           # User templates
├── static/              # Static files
│   ├── css/
│   │   └── style.css    # Main stylesheet
│   └── js/
│       └── main.js      # JavaScript functionality
└── media/               # User-uploaded files
    ├── course_thumbnails/
    ├── course_materials/
    └── profiles/
```

## Installation & Setup

1. **Install dependencies:**
   ```bash
   poetry install
   ```

2. **Run migrations:**
   ```bash
   poetry run python manage.py migrate
   ```

3. **Create a superuser:**
   ```bash
   poetry run python manage.py createsuperuser
   ```

4. **Create media directories:**
   ```bash
   mkdir -p media/course_thumbnails media/course_materials media/profiles
   ```

5. **Run the development server:**
   ```bash
   poetry run python manage.py runserver
   ```

6. **Access the application:**
   - Website: http://localhost:8000/
   - Admin panel: http://localhost:8000/admin/

## User Roles

### Student (Default)
- Can browse and enroll in courses
- Can view and download course materials
- Cannot create courses

### Author
- All student permissions
- Can create and manage their own courses
- Can upload course materials
- Access to author dashboard

### Admin (Superuser)
- Full access to Django admin panel
- Can manage all users and content
- Can change user roles

## Key URLs

- `/` - Home page
- `/courses/` - Browse all courses
- `/courses/<slug>/` - Course detail page
- `/courses/<slug>/lessons/<id>/` - Lesson detail page
- `/my-courses/` - User's enrolled courses
- `/author/dashboard/` - Author dashboard (authors only)
- `/users/register/` - User registration
- `/users/login/` - User login
- `/users/profile/` - User profile
- `/admin/` - Django admin panel

## Database Models

### User
- Custom user model extending Django's AbstractUser
- Fields: username, email, role, bio, profile_picture

### Course
- Fields: title, slug, description, author, difficulty, thumbnail, is_published
- Related: lessons, enrollments

### Lesson
- Fields: title, content, order, course
- Related: materials

### Material
- Fields: title, file, material_type, description, lesson
- Types: PDF, Video, Document, Other

### Enrollment
- Fields: user, course, enrolled_at
- Tracks which users are enrolled in which courses

## Service Layer

The application follows a service-oriented architecture:

### UserService
- User registration and authentication
- Profile management
- User queries

### CourseService
- Course CRUD operations
- Course search and filtering
- Author course management

### LessonService
- Lesson CRUD operations
- Lesson ordering

### MaterialService
- Material upload and management
- File handling

### EnrollmentService
- Course enrollment/unenrollment
- Enrollment queries

## Security Features

- User authentication required for sensitive operations
- Authors can only manage their own courses
- Enrollment verification for accessing lessons
- File download permissions checked
- CSRF protection on all forms
- Password validation

## Customization

### Adding New Course Difficulties
Edit `courses/models.py` - Course model - DIFFICULTY_CHOICES

### Adding New Material Types
Edit `courses/models.py` - Material model - MATERIAL_TYPES

### Styling
Modify `static/css/style.css` for visual customization

### JavaScript Behavior
Modify `static/js/main.js` for interactive features

## Production Deployment

Before deploying to production:

1. Change `DEBUG = False` in settings.py
2. Set a secure `SECRET_KEY`
3. Configure `ALLOWED_HOSTS`
4. Use a production database (PostgreSQL recommended)
5. Configure static file serving
6. Set up media file storage (S3, etc.)
7. Enable HTTPS
8. Configure email backend for notifications

## Technologies Used

- **Backend:** Django 6.0
- **Database:** SQLite (development) / PostgreSQL (production)
- **Image Processing:** Pillow
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Package Management:** Poetry

## Contributing

This is a learning platform project. Feel free to extend it with:
- Video player integration
- Progress tracking
- Certificates
- Quiz functionality
- Discussion forums
- Payment integration
- API endpoints (Django REST Framework)

## License

This project is open-source and available for educational purposes.
