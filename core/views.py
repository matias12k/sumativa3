from django.shortcuts import render

# Create your views here.
def home(request):
    
    return render(request, 'core/E1_matias_barraza_S2.html')


def accion(request):
    return render(request, 'core/accion.html')



def terror(request):
    return render(request, 'core\Terror.html')


def estrategia(request):
    return render(request, 'core/Estrategia.html')


def deporte(request):
    return render(request, 'core/Deporte.html')


def registro(request):
    return render(request,'core\Registro.html')


def inicio_sesion(request):
    return render(request, 'core/inicio_sesion.html')