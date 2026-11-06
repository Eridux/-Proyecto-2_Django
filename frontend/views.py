from django.shortcuts import render

type values = str | dict
# Create your views here.
def frontend(request):
    menues: dict[str,str] = {
        'inicio': 'Inicio',
        'frontend': 'Frontend',
        'backend': 'Backend',
     }
     
    datos: dict [str, values] = {
        'titulo': 'Página de Frontend',
        'encabezado': 'Tecnologías de lado de el Cliente',
        'empresa': 'Tecnologías Web',
        'menues': menues,
    }

    return render(request, 'frontend/frontend.html', datos)