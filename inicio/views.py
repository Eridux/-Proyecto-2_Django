from django.shortcuts import render

type values = str | dict

# Create your views here.
def inicio(request):
    menues: dict[str,str] = {
        'inicio': 'Inicio',
        'frontend': 'Frontend',
        'backend': 'Backend',
    }
    
    
    
    datos: dict [str, values] = {
        'titulo': 'Página de Inicio',
        'encabezado': 'Tecnologías Web (Frontend / Backend)',
        'empresa': 'Tecnologías Web',
        'menues': menues,
    }

    return render(request, 'inicio/index.html', datos)