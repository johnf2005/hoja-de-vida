# Comandos Útiles de Django

## 🚀 Iniciar desarrollo

```bash
# Activar entorno virtual
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# Navegar a proyecto
cd mi_proyecto

# Ejecutar servidor
python manage.py runserver
```

## 📦 Gestión de Base de Datos

```bash
# Crear migraciones
python manage.py makemigrations

# Aplicar migraciones
python manage.py migrate

# Ver migraciones
python manage.py showmigrations

# Revertir migraciones
python manage.py migrate [app] [número_migracion]

# Ver SQL de migraciones
python manage.py sqlmigrate [app] [número_migracion]
```

## 👤 Usuarios y Administración

```bash
# Crear superusuario
python manage.py createsuperuser

# Cambiar contraseña
python manage.py changepassword [username]

# Crear usuario normal
python manage.py shell
# >>> from django.contrib.auth.models import User
# >>> User.objects.create_user('username', 'email@example.com', 'password')
```

## 📁 Archivos Estáticos

```bash
# Recolectar archivos estáticos
python manage.py collectstatic

# Recolectar sin confirmar
python manage.py collectstatic --noinput

# Limpiar archivos estáticos antiguos
python manage.py collectstatic --clear
```

## 📱 Crear Aplicación Django

```bash
# Crear nueva app
python manage.py startapp [nombre_app]

# Añadir a INSTALLED_APPS en settings.py
INSTALLED_APPS = [
    ...
    '[nombre_app]',
]
```

## 🧪 Testing

```bash
# Ejecutar todas las pruebas
python manage.py test

# Ejecutar pruebas de una app
python manage.py test [nombre_app]

# Ejecutar pruebas con verbosidad
python manage.py test --verbosity=2
```

## 🔍 Comandos Útiles

```bash
# Entrar en shell interactivo
python manage.py shell

# Ejecutar comando personalizado
python manage.py [custom_command]

# Listar todas las URLs
python manage.py show_urls

# Verificar configuración
python manage.py check

# Generar diagrama de modelos (django-extensions)
python manage.py graph_models -a -o models.png

# Limpiar sesiones expiradas
python manage.py clearsessions

# Hacer copia de seguridad de datos
python manage.py dumpdata > backup.json

# Restaurar datos
python manage.py loaddata backup.json
```

## 🐛 Debugging

```bash
# Entrar en shell y ver queries
from django.db import connection
from django.test.utils import CaptureQueriesContext

with CaptureQueriesContext(connection) as context:
    # Tu código
print(len(context.captured_queries))  # Número de queries
for query in context.captured_queries:
    print(query['sql'])
```

## 📦 Dependencias

```bash
# Listar paquetes instalados
pip freeze

# Actualizar requirements.txt
pip freeze > requirements.txt

# Instalar desde requirements.txt
pip install -r requirements.txt

# Instalar paquete específico
pip install [nombre_paquete]==[versión]
```

## 🚨 Solucionar Problemas

```bash
# Verificar configuración de Django
python manage.py check

# Verificar migraciones pendientes
python manage.py showmigrations --list

# Ver rutas URL configuradas
python manage.py show_urls

# Limpiar caché de Python
find . -type d -name __pycache__ -exec rm -r {} +
find . -type f -name "*.pyc" -delete
```

## 🌐 Producción (Render)

```bash
# En settings.py, asegúrate que:
DEBUG = False
ALLOWED_HOSTS = ['tu-app.onrender.com']

# Comandos para deployment
python manage.py collectstatic --noinput
python manage.py migrate --noinput
gunicorn mi_proyecto.wsgi:application
```
