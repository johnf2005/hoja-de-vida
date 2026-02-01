# 📄 Hoja de Vida Virtual - Django Project

Una aplicación Django para crear y gestionar tu hoja de vida virtual con conexión a base de datos PostgreSQL en Render.

## 🚀 Características

- ✅ Interfaz de administración Django
- ✅ Base de datos PostgreSQL en Render
- ✅ Archivos estáticos optimizados con WhiteNoise
- ✅ Configuración de seguridad para producción
- ✅ CORS habilitado para frontend separado
- ✅ Logging configurado
- ✅ Soporte para PDF con ReportLab

## 📋 Requisitos Previos

- Python 3.11+
- PostgreSQL (para desarrollo local)
- Cuenta en Render.com

## 🔧 Instalación Local

### 1. Clonar el repositorio

```bash
git clone <tu-repo>
cd "hoja de vida"
```

### 2. Crear entorno virtual

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

Crear archivo `.env` en la carpeta `mi_proyecto`:

```env
SECRET_KEY=tu_clave_secreta_muy_larga_y_aleatoria
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3
CORS_ALLOWED_ORIGINS=http://localhost:3000,http://127.0.0.1:3000
```

### 5. Ejecutar migraciones

```bash
cd mi_proyecto
python manage.py migrate
```

### 6. Crear superusuario

```bash
python manage.py createsuperuser
```

### 7. Ejecutar servidor de desarrollo

```bash
python manage.py runserver
```

Visita: `http://localhost:8000/admin`

## 📦 Despliegue en Render

### 1. Conectar repositorio a Render

1. Ve a [Render.com](https://render.com)
2. Conecta tu repositorio GitHub
3. Crea un nuevo **Web Service**

### 2. Configurar variables de entorno en Render

En el panel de Render, agrega:

```
DEBUG=False
SECRET_KEY=<genera-una-clave-segura>
ALLOWED_HOSTS=tu-app.onrender.com
DATABASE_URL=<conexión-postgresql-render>
CORS_ALLOWED_ORIGINS=https://tu-frontend.onrender.com
```

### 3. Build Command

```bash
pip install -r requirements.txt && python manage.py collectstatic --noinput && python manage.py migrate --noinput
```

### 4. Start Command

```bash
gunicorn mi_proyecto.wsgi:application
```

## 📁 Estructura del Proyecto

```
hoja-de-vida/
├── build.sh                    # Script de deployment
├── runtime.txt                 # Versión de Python para Render
├── requirements.txt            # Dependencias Python
├── wsgi.py                     # WSGI para Render
├── render.yaml                 # Configuración de Render
├── mi_proyecto/                # Proyecto Django
│   ├── manage.py
│   ├── .env                    # Variables de entorno (NO subir)
│   ├── .gitignore
│   ├── db.sqlite3
│   ├── mi_proyecto/
│   │   ├── settings.py         # Configuración (ya actualizada)
│   │   ├── urls.py
│   │   ├── wsgi.py
│   │   └── asgi.py
│   ├── templates/              # (crear carpeta)
│   └── static/                 # (crear carpeta)
└── hoja-de-vida/               # Repo Git
```

## 🔐 Seguridad

- ✅ SECRET_KEY en variables de entorno
- ✅ DEBUG=False en producción
- ✅ ALLOWED_HOSTS configurado
- ✅ HTTPS redirect en producción
- ✅ CSRF protection habilitada
- ✅ XSS filter activo
- ✅ Cookies seguras en producción

## 📝 Próximos Pasos

1. **Crear app principal**:
   ```bash
   python manage.py startapp portfolio
   ```

2. **Crear modelos** para datos de la hoja de vida

3. **Crear templates HTML** en la carpeta `/templates`

4. **Configurar URLs** en `urls.py`

5. **Agregar estilos CSS** en la carpeta `/static/css`

## 🤝 Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request.

## 📄 Licencia

Este proyecto está bajo licencia MIT.

## 📞 Soporte

Para reportar problemas o sugerencias, abre un issue en el repositorio.
