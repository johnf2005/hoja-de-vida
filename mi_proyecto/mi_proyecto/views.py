from django.shortcuts import render
from portfolio.models import Perfil, Educacion, Experiencia, Habilidad


def index(request):
    # Obtener perfil (si no existe, usar datos por defecto)
    try:
        perfil = Perfil.objects.first()
        if not perfil:
            perfil = {
                'nombre': 'Tu Nombre Completo',
                'titulo': 'Desarrollador/a Python / Django',
                'resumen': 'Resumen breve sobre tu experiencia y objetivos profesionales.',
                'email': 'tu.email@ejemplo.com',
                'telefono': '+57 300 000 0000',
                'ubicacion': 'Ciudad, País',
            }
    except:
        perfil = {
            'nombre': 'Tu Nombre Completo',
            'titulo': 'Desarrollador/a Python / Django',
            'resumen': 'Resumen breve sobre tu experiencia y objetivos profesionales.',
            'email': 'tu.email@ejemplo.com',
            'telefono': '+57 300 000 0000',
            'ubicacion': 'Ciudad, País',
        }

    # Obtener educación
    educacion = Educacion.objects.all().order_by('-anio_fin', '-anio_inicio')

    # Obtener experiencia
    experiencia = Experiencia.objects.all().order_by('-fecha_fin', '-fecha_inicio')

    # Obtener habilidades
    habilidades = Habilidad.objects.all().order_by('orden')

    datos = {
        'perfil': perfil,
        'educacion': educacion,
        'experiencia': experiencia,
        'habilidades': habilidades,
    }

    return render(request, 'index.html', {'datos': datos})

