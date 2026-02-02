#!/usr/bin/env python
import os
import sys
import django

try:
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mi_proyecto.settings')
    django.setup()
    
    from django.contrib.auth.models import User
    
    username = 'adminjohn'
    email = 'admin@hojadevida.com'
    password = 'admin123456'
    
    # Intentar obtener el usuario
    try:
        user = User.objects.get(username=username)
        print(f'ℹ️  Usuario "{username}" ya existe')
        # Actualizar permisos si es necesario
        if not user.is_staff or not user.is_superuser:
            user.email = email
            user.is_staff = True
            user.is_superuser = True
            user.set_password(password)
            user.save()
            print(f'✅ Permisos de "{username}" actualizados')
        else:
            print(f'✅ Usuario "{username}" ya tiene permisos correctos')
    except User.DoesNotExist:
        # Crear nuevo usuario
        user = User.objects.create_superuser(
            username=username,
            email=email,
            password=password
        )
        print(f'✅ Superuser "{username}" creado exitosamente')
        
except Exception as e:
    print(f'❌ Error al crear/actualizar superuser: {str(e)}')
    print(f'Tipo de error: {type(e).__name__}')
    sys.exit(1)
