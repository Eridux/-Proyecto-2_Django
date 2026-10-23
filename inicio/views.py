from django.shortcuts import render

# Create your views here.
def inicio(request):
    datos: dict [str, str] = {
        'titulo': 'Pagina de inicio',
        'encabezado': 'Bienvenidos a mi sitio web'
    }

    return render(request, 'inicio/index.html', datos)