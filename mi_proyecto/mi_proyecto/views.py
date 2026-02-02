from django.shortcuts import render
from portfolio.models import DatosPersonales, ExperienciaLaboral, CursoRealizado


def index(request):
    # Obtener primer perfil activo
    perfil = DatosPersonales.objects.filter(perfilactivo=1).first()
    
    if not perfil:
        # Si no hay perfil, mostrar mensaje
        datos = {
            'perfil': None,
            'experiencia': [],
            'cursos': [],
        }
        return render(request, 'index.html', {'datos': datos})
    
    # Obtener experiencia visible
    experiencia = ExperienciaLaboral.objects.filter(
        idperfilconqueestaactivo=perfil,
        activarparaqueseveaenfront=True
    ).order_by('-fechafingestion', '-fechainiciogestion')
    
    # Obtener cursos visibles
    cursos = CursoRealizado.objects.filter(
        idperfilconqueestaactivo=perfil,
        activarparaqueseveaenfront=True
    ).order_by('-fechafin', '-fechainicio')

    datos = {
        'perfil': perfil,
        'experiencia': experiencia,
        'cursos': cursos,
    }

    return render(request, 'index.html', {'datos': datos})

