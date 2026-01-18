# Quick Start Guide

## Getting Started in 3 Easy Steps

### Step 1: Install Dependencies
```bash
poetry install
```

### Step 2: Set Up Database
```bash
poetry run python manage.py migrate
```

### Step 3: Create Sample Data (Optional but Recommended)
```bash
poetry run python manage.py create_sample_data
```

This creates:
- **Admin user:** admin/admin123
- **Author 1:** john_doe/author123
- **Author 2:** jane_smith/author123
- **Student:** student/student123
- **4 sample courses** with lessons

### Step 4: Run the Server
```bash
./start.sh
```
Or manually:
```bash
poetry run python manage.py runserver
```

### Step 5: Access the Application
- **Website:** http://localhost:8000/
- **Admin Panel:** http://localhost:8000/admin/

## First-Time Setup

### Creating Your Own Admin User
```bash
poetry run python manage.py createsuperuser
```
Follow the prompts to create your admin account.

## Features Tour

### As a Student:
1. Register at `/users/register/` and choose "Student" role
2. Browse courses at `/courses/`
3. Click on a course to view details
4. Enroll in courses
5. View lessons and download materials
6. Track your enrolled courses at `/my-courses/`

### As an Author:
1. Register at `/users/register/` and choose "Author" role
2. Go to Author Dashboard at `/author/dashboard/`
3. Create a new course
4. Add lessons to your course
5. Upload materials (PDFs, videos, documents)
6. Publish your course when ready

### As an Admin:
1. Login to admin panel at `/admin/`
2. Manage all users, courses, lessons, and materials
3. Change user roles
4. Monitor platform activity

## Project Structure Overview

```
├── courses/           # Course management
├── users/            # User authentication
├── templates/        # HTML templates
├── static/           # CSS & JavaScript
├── media/            # User uploads
└── main/             # Project settings
```

## Common Commands

```bash
# Run development server
poetry run python manage.py runserver

# Create migrations
poetry run python manage.py makemigrations

# Apply migrations
poetry run python manage.py migrate

# Create superuser
poetry run python manage.py createsuperuser

# Create sample data
poetry run python manage.py create_sample_data

# Access Django shell
poetry run python manage.py shell
```

## Troubleshooting

### Port Already in Use
```bash
# Use a different port
poetry run python manage.py runserver 8080
```

### Database Locked
```bash
# Delete db.sqlite3 and recreate
rm db.sqlite3
poetry run python manage.py migrate
poetry run python manage.py create_sample_data
```

### Static Files Not Loading
```bash
# Collect static files
poetry run python manage.py collectstatic
```

## Next Steps

1. ✅ Set up the project
2. ✅ Create sample data
3. ✅ Explore the website
4. Start creating your own courses!
5. Customize the styling in `static/css/style.css`
6. Add more features as needed

## Need Help?

Check the main README.md for detailed documentation about:
- Project architecture
- Database models
- Service layer
- URL structure
- Security features
- Production deployment

Enjoy building your e-learning platform! 🚀
