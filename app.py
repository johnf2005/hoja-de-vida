"""
Render expects 'app' module at root.
This file bridges to the Django WSGI application.
"""
import os
import sys

# Add mi_proyecto to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'mi_proyecto'))

# Import Django WSGI application
from mi_proyecto.wsgi import application

# Also expose as 'app' for Render's default gunicorn app:app
app = application

__all__ = ['application', 'app']
