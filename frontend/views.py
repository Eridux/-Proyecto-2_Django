from django.shortcuts import render

# Create your views here.
def frontend(request):
    datos: dict [str, str] = {
        'titulo': 'Pagina de Frontend',
        'encabezado': 'Tecnologías de lado de el Cliente'
    }

    return render(request, 'frontend/frontend.html', datos)