#!/bin/bash
set -o errexit

echo "Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

echo "Collecting static files..."
cd mi_proyecto
python manage.py collectstatic --noinput

echo "Running migrations..."
python manage.py migrate --noinput

echo "Build completed successfully!"