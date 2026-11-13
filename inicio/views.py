from django.shortcuts import render
from django.db.models.manager import BaseManager
from .models import Inicio
type values = str | dict | list | BaseManager

# Create your views here.
def inicio(request):
    #tarjetas: list[int] = list(range(8))
    tarjetas: BaseManager = Inicio.objects.all()
    
    menues: dict[str,str] = {
        'inicio': 'Inicio',
        'frontend': 'Frontend',
        'backend': 'Backend',
    }
    
    
    pie: dict[str,str] = {
        'primero': '#instagram',
        'segundo': '#youtube',
        'tercero': '#x',
        'cuarto': '#linkedin',
        'quinto': '#github'
    }
    datos: dict [str, values] = {
        'titulo': 'Página de Inicio',
        'encabezado': 'Tecnologías Web (Frontend / Backend)',
        'empresa': 'Tecnologías Web',
        'menues': menues,
        'tarjetas': tarjetas,
        'pie': pie,
    }

    return render(request, 'inicio/index.html', datos)