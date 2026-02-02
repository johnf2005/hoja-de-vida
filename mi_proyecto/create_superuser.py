import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_proyecto.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Crear superuser solo si no existe
if not User.objects.filter(username='adminjohn').exists():
    User.objects.create_superuser(
        username='adminjohn',
        email='admin@hojadevida.com',
        password='admin123456'
    )
    print('✅ Superuser "adminjohn" creado exitosamente')
else:
    print('ℹ️ Superuser "adminjohn" ya existe')
