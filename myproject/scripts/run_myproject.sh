cd ~/MCON-357-Spring-2025/myproject
gunicorn myproject.wsgi:application --bind 0.0.0.0:8000 &
