from django.shortcuts import render
from .models import Formulario
from django.http import JsonResponse
from .models import Usuario
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
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

def agregar_usuario(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        usuario = request.POST['usuario']
        correo = request.POST['correo']
        contrasena = request.POST['contrasena']
        telefono = request.POST['telefono']
        direccion = request.POST['direccion']
        Formulario.objects.create(nombre=nombre, usuario=usuario)
        return render(request, 'core/accion.html')
        
    #    if nombre and usuario and correo and contrasena and telefono and direccion:
     #       Formulario.objects.create (nombre= nombre, usuario=usuario, correo=correo, contrasena=contrasena, telefono=telefono, direccion=direccion)
    #      Formulario.save()
    else:  
        return render(request, 'core/inicio_sesion.html')

def usuarios(request):
    usuarios = Usuario.objects.all().values()
    return JsonResponse({'usuarios': list(usuarios)})


@api_view(['GET'])
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
def usuarios(request):
    usuarios = Usuario.objects.all()
    serializer = Usuario.Serializer(usuarios, many=True)
    return Response(serializer.data)