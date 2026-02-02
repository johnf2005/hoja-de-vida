import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_proyecto.settings')
django.setup()

from django.conf import settings

print("=" * 60)
print("DIAGNÓSTICO DE BASE DE DATOS")
print("=" * 60)
print(f"DATABASE_URL env var: {os.environ.get('DATABASE_URL', 'NO CONFIGURADA')}")
print(f"Engine: {settings.DATABASES['default']['ENGINE']}")
print(f"Name: {settings.DATABASES['default']['NAME']}")
print(f"Host: {settings.DATABASES['default'].get('HOST', 'N/A')}")
print(f"Port: {settings.DATABASES['default'].get('PORT', 'N/A')}")
print(f"User: {settings.DATABASES['default'].get('USER', 'N/A')}")
print("=" * 60)

# Verificar si la BD usa PostgreSQL o SQLite
if 'sqlite' in settings.DATABASES['default']['ENGINE']:
    print("⚠️  ADVERTENCIA: Usando SQLite - PostgreSQL NO conectado")
    print("⚠️  Las migraciones no se aplicarán correctamente")
elif 'postgres' in settings.DATABASES['default']['ENGINE']:
    print("✅ PostgreSQL detectado correctamente")
else:
    print(f"⚠️  Motor de BD desconocido: {settings.DATABASES['default']['ENGINE']}")
