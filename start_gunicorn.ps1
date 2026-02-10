# PowerShell script to start Gunicorn on Windows

Write-Host "Starting Gunicorn server..." -ForegroundColor Green

# Run migrations
Write-Host "Running migrations..." -ForegroundColor Yellow
poetry run python manage.py migrate

# Collect static files
Write-Host "Collecting static files..." -ForegroundColor Yellow
poetry run python manage.py collectstatic --noinput

# Start Gunicorn
Write-Host "Starting Gunicorn on 0.0.0.0:8000..." -ForegroundColor Green
poetry run gunicorn main.wsgi:application --config gunicorn.conf.py --reload
