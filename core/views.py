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

def agregar_usuario(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        usuario = request.POST['usuario']
        correo = request.POST['correo']
        contrasena = request.POST['contrasena']
        telefono = request.POST['telefono']
        direccion = request.POST['direccion']
        
        if nombre and usuario and correo and contrasena and telefono and direccion
        formulario = Formulario(nombre=nombre, usuario=usuario, correo=correo, contrasena=contrasena, telefono=telefono, direccion=direccion)
        formulario.save()  
    return render(request, 'core/inicio_sesion.html')
