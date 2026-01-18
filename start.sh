#!/bin/bash

echo "Starting E-Learning Platform..."
echo "================================"

# Check if virtual environment is activated
if [ -z "$VIRTUAL_ENV" ]; then
    echo "Activating virtual environment..."
    poetry shell
fi

# Run migrations
echo "Running migrations..."
poetry run python manage.py migrate

# Start the server
echo "Starting development server..."
echo "Access the application at: http://localhost:8000/"
echo "Press Ctrl+C to stop the server"
echo "================================"
poetry run python manage.py runserver
