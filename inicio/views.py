from django.shortcuts import render

# Create your views here.
def inicio(request):
    datos: dict [str, str] = {
        'titulo': 'Página de Inicio',
        'encabezado': 'Tecnologías Web (Frontend / Backend)',
        'empresa': 'Tecnologías Web',
    }

    return render(request, 'inicio/index.html', datos)