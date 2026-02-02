from django.shortcuts import render


def home(request):
    # Example resume data — edit as needed or load from DB
    resume = {
        'name': 'Tu Nombre',
        'title': 'Desarrollador / Diseñador',
        'contact': {
            'email': 'tu@email.com',
            'phone': '+57 300 0000000',
            'location': 'Ciudad, País'
        },
        'summary': 'Profesional con experiencia en desarrollo web y tecnologías Django, Python y frontend.',
        'education': [
            {'degree': 'Ingeniería en Sistemas', 'institution': 'Universidad X', 'year': '2020'},
        ],
        'experience': [
            {'role': 'Desarrollador Web', 'company': 'Empresa Y', 'period': '2021 - Presente', 'details': 'Trabajo en proyectos Django y despliegues.'},
        ],
        'skills': ['Python', 'Django', 'HTML', 'CSS', 'JavaScript', 'PostgreSQL'],
    }
    return render(request, 'portfolio/index.html', {'resume': resume})
