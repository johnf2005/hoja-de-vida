import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_proyecto.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

# Crear o actualizar superuser
user, created = User.objects.get_or_create(
    username='adminjohn',
    defaults={
        'email': 'admin@hojadevida.com',
        'is_staff': True,
        'is_superuser': True
    }
)

if created:
    user.set_password('admin123456')
    user.save()
    print('✅ Superuser "adminjohn" creado exitosamente')
else:
    # Actualizar si ya existe
    user.email = 'admin@hojadevida.com'
    user.is_staff = True
    user.is_superuser = True
    user.set_password('admin123456')
    user.save()
    print('✅ Superuser "adminjohn" actualizado exitosamente')
