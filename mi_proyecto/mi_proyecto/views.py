from django.shortcuts import render
from django.db import OperationalError, DatabaseError
from portfolio.models import (
    DatosPersonales, ExperienciaLaboral, CursoRealizado, Documento,
    ProductoAcademico, ProductoLaboral, Reconocimiento, VentaGarage
)


def index(request):
    try:
        # Obtener primer perfil activo
        perfil = DatosPersonales.objects.filter(perfilactivo=1).first()

        if not perfil:
            datos = {
                'perfil': None, 'experiencia': [], 'cursos': [], 'documentos': [],
                'productos_academicos': [], 'productos_laborales': [],
                'reconocimientos': [], 'ventas_garage': []
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

        # Obtener documentos visibles
        documentos = Documento.objects.filter(
            idperfilconqueestaactivo=perfil,
            activarparaqueseveaenfront=True
        ).order_by('orden')

        # Obtener productos académicos visibles
        productos_academicos = ProductoAcademico.objects.filter(
            activarparaqueseveaenfront=True
        ).order_by('-fechacreacion')

        # Obtener productos laborales visibles
        productos_laborales = ProductoLaboral.objects.filter(
            idperfilconqueestaactivo=perfil,
            activarparaqueseveaenfront=True
        ).order_by('-fechacreacion')

        # Obtener reconocimientos visibles
        reconocimientos = Reconocimiento.objects.filter(
            idperfilconqueestaactivo=perfil,
            activarparaqueseveaenfront=True
        ).order_by('-fechareconocimiento')

        # Obtener ventas garage visibles
        ventas_garage = VentaGarage.objects.filter(
            activarparaqueseveaenfront=True
        ).order_by('-fechacreacion')

    except (OperationalError, DatabaseError):
        # DB not ready / migrations missing: render page layout without DB data
        datos = {
            'perfil': None, 'experiencia': [], 'cursos': [], 'documentos': [],
            'productos_academicos': [], 'productos_laborales': [],
            'reconocimientos': [], 'ventas_garage': []
        }
        return render(request, 'index.html', {'datos': datos})

    datos = {
        'perfil': perfil,
        'experiencia': experiencia,
        'cursos': cursos,
        'documentos': documentos,
        'productos_academicos': productos_academicos,
        'productos_laborales': productos_laborales,
        'reconocimientos': reconocimientos,
        'ventas_garage': ventas_garage,
    }

    return render(request, 'index.html', {'datos': datos})

