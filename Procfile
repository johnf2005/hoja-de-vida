web: bash -c "cd mi_proyecto && python manage.py collectstatic --noinput && gunicorn mi_proyecto.wsgi:application --workers 1 --timeout 60"
