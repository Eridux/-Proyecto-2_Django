from django.shortcuts import render
from django.db.models.manager import BaseManager
from .models import Frontend

type values = str | dict | BaseManager
# Create your views here.
def frontend(request):
    tarjetas: BaseManager = Frontend.objects.all()
    
    menues: dict[str,str] = {
        'inicio': 'Inicio',
        'frontend': 'Frontend',
        'backend': 'Backend',
     }
     
    pie: dict[str,str] = {
             'primero': '#html',
             'segundo': '#css',
             'tercero': '#js',
             'cuarto': '#tailwindcss',
             'quinto': '#react'
         }
    datos: dict [str, values] = {
        'titulo': 'Página de Frontend',
        'encabezado': 'Tecnologías de lado de el Cliente',
        'empresa': 'Tecnologías Web',
        'menues': menues,
        'tarjetas': tarjetas,
        'pie': pie,
    }

    return render(request, 'frontend/frontend.html', datos)