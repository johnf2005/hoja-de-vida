#!/bin/bash
set -o errexit

echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Collecting static files..."
cd mi_proyecto
python check_db.py

echo "Running migrations..."
python manage.py migrate --noinput --verbosity 3

echo "Creating admin user..."
python manage.py create_admin

echo "Collecting static files..."
python manage.py collectstatic --noinput

echo "Build completed successfully!"