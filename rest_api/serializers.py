from rest_framework import serializers
from core.models import Formulario, Rol, Usuario

class FormularioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Formulario
        fields = ['nombre', 'usuario', 'correo', 'contrasena', 'telefono', 'direccion']


class RolSerializers(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = ['id_rol', 'nombre']

class UsuarioSerializers(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id_usuario', 'correo', 'clave', 'estatus', 'rut', 'rol']



       