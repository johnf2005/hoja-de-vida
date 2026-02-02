from django.shortcuts import render
from django.db import OperationalError, DatabaseError
from portfolio.models import DatosPersonales, ExperienciaLaboral, CursoRealizado, Documento


def index(request):
    try:
        # Obtener primer perfil activo
        perfil = DatosPersonales.objects.filter(perfilactivo=1).first()

        if not perfil:
            datos = {'perfil': None, 'experiencia': [], 'cursos': [], 'documentos': []}
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
    except (OperationalError, DatabaseError):
        # DB not ready / migrations missing: render page layout without DB data
        datos = {'perfil': None, 'experiencia': [], 'cursos': [], 'documentos': []}
        return render(request, 'index.html', {'datos': datos})

    datos = {
        'perfil': perfil,
        'experiencia': experiencia,
        'cursos': cursos,
        'documentos': documentos,
    }

    return render(request, 'index.html', {'datos': datos})

