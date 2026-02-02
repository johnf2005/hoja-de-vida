from django.shortcuts import render


def index(request):
    # Datos de ejemplo; adapta esto para cargar desde tus modelos o la base de datos
    datos = {
        'nombre': 'Tu Nombre Completo',
        'titulo': 'Desarrollador/a Python / Django',
        'resumen': 'Resumen breve sobre tu experiencia y objetivos profesionales.',
        'datos_personales': {
            'Email': 'tu.email@ejemplo.com',
            'Teléfono': '+57 300 000 0000',
            'Ubicación': 'Ciudad, País',
        },
        'educacion': [
            {'titulo': 'Ingeniería de Sistemas', 'centro': 'Universidad X', 'anio': '2018-2022'},
        ],
        'experiencia': [
            {'cargo': 'Desarrollador Backend', 'empresa': 'Empresa Y', 'periodo': '2023 - Presente', 'detalle': 'Trabajo con Django y APIs REST.'},
        ],
        'habilidades': ['Python', 'Django', 'REST', 'PostgreSQL', 'Docker'],
    }

    return render(request, 'index.html', {'datos': datos})
