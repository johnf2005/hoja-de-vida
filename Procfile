web: bash -lc "cd mi_proyecto && python manage.py migrate --noinput --verbosity 3 && python manage.py collectstatic --noinput && gunicorn app:app --workers 1 --timeout 60"
