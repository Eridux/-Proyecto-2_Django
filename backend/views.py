from django.shortcuts import render

type values = str | dict

# Create your views here.
def backend(request):
    menues: dict[str,str] = {
        'inicio': 'Inicio',
        'frontend': 'Frontend',
        'backend': 'Backend',
     }    
    
    datos: dict [str, values] = {
        'titulo': 'Página de Backend',
        'encabezado': 'Tecnologías de lado de el Servidor',
        'empresa': 'Tecnologías Web',
        'menues': menues,        
    }

    return render(request, 'backend/backend.html', datos)