from django.shortcuts import render
from django.db.models.manager import BaseManager
from .models import Backend

type values = str | dict | BaseManager

# Create your views here.
def backend(request):
    tarjetas: BaseManager = Backend.objects.all()
    
    menues: dict[str,str] = {
        'inicio': 'Inicio',
        'frontend': 'Frontend',
        'backend': 'Backend',
     }    
    
    pie: dict[str,str] = {
            'primero': '#php',
            'segundo': '#python',
            'tercero': '#node',
            'cuarto': '#laravel',
            'quinto': '#django'
        }
    datos: dict [str, values] = {
        'titulo': 'Página de Backend',
        'encabezado': 'Tecnologías de lado de el Servidor',
        'empresa': 'Tecnologías Web',
        'menues': menues, 
        'tarjetas': tarjetas, 
        'pie': pie,     
    }

    return render(request, 'backend/backend.html', datos)