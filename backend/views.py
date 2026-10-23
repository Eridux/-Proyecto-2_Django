from django.shortcuts import render

# Create your views here.
def backend(request):
    datos: dict [str, str] = {
        'titulo': 'Pagina de Backend',
        'encabezado': 'Tecnologías de lado de el Servidor'
    }

    return render(request, 'backend/backend.html', datos)