from django.shortcuts import render
from portfolio.models import DatosPersonales, ExperienciaLaboral, CursoRealizado, Documento


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

    # Obtener documentos visibles (para menú)
    documentos = Documento.objects.filter(
        idperfilconqueestaactivo=perfil,
        activarparaqueseveaenfront=True
    ).order_by('orden')

    datos = {
        'perfil': perfil,
        'experiencia': experiencia,
        'cursos': cursos,
        'documentos': documentos,
    }

    return render(request, 'index.html', {'datos': datos})

