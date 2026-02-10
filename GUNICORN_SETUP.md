# Gunicorn Setup Guide

## Configuration

Gunicorn has been configured for the e-learning site with the following files:

- **gunicorn.conf.py**: Main configuration file with production-ready settings
- **start_gunicorn.sh**: Bash script to start the server (Linux/Mac)
- **start_gunicorn.ps1**: PowerShell script to start the server (Windows)

## Running Gunicorn

### Option 1: Using the PowerShell script (Windows)

```powershell
.\start_gunicorn.ps1
```

### Option 2: Using the Bash script (Linux/Mac)

```bash
chmod +x start_gunicorn.sh
./start_gunicorn.sh
```

### Option 3: Manual command (Poetry)

```bash
poetry run gunicorn main.wsgi:application --config gunicorn.conf.py
```

### Option 4: Manual command (Standard)

```bash
gunicorn main.wsgi:application --config gunicorn.conf.py
```

## Configuration Details

### Workers

- **Workers**: `(CPU cores * 2) + 1` (automatically calculated)
- **Worker Class**: sync
- **Timeout**: 30 seconds
- **Keepalive**: 2 seconds

### Binding

- **Host**: 0.0.0.0 (all interfaces)
- **Port**: 8000

### Logging

- Access logs and error logs output to stdout/stderr
- Log level: info

## Production Deployment

For production, update the following in `main/settings.py`:

1. Set `DEBUG = False`
2. Set `SECRET_KEY` to a secure random string (use environment variable)
3. Update `ALLOWED_HOSTS` with your domain names
4. Configure a proper database (PostgreSQL recommended)
5. Set up a reverse proxy (Nginx or Apache)
6. Remove `--reload` flag from gunicorn command

### Example Production Command

```bash
gunicorn main.wsgi:application \
    --config gunicorn.conf.py \
    --workers 4 \
    --bind unix:/tmp/gunicorn.sock \
    --log-level error
```

## Environment Variables (Recommended for Production)

Create a `.env` file:

```env
DEBUG=False
SECRET_KEY=your-secret-key-here
DATABASE_URL=postgresql://user:password@localhost/dbname
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
```

## Monitoring

Check if Gunicorn is running:

```bash
# Linux/Mac
ps aux | grep gunicorn

# Windows (PowerShell)
Get-Process | Where-Object {$_.ProcessName -like "*python*"}
```

## Stopping Gunicorn

Press `Ctrl+C` in the terminal where Gunicorn is running.

For background processes:

```bash
# Find the process
ps aux | grep gunicorn

# Kill the master process
kill -TERM <master_pid>
```
