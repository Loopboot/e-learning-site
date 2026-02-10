#!/bin/bash

# Start script for Gunicorn

echo "Starting Gunicorn server..."

# Activate virtual environment if using one
# source venv/bin/activate

# Run migrations
echo "Running migrations..."
python manage.py migrate

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start Gunicorn
echo "Starting Gunicorn on 0.0.0.0:8000..."
gunicorn main.wsgi:application \
    --config gunicorn.conf.py \
    --reload
