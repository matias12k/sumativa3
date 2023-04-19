from django.db import models

# Create your models here.


class Formulario(models.Model):
    nombre = models.CharField(max_length=100)
    usuario = models.CharField(max_length=30)
    correo = models.CharField(max_length=100)
    contrasena =models.CharField(max_length=10)
    telefono = models.CharField(max_length=100)
    direccion = models.CharField(max_length=100)

    def __str__(self):
        return self.usuario


class Rol (models.Model):
    id_Rol = models.AutoField(primary_key=True, verbose_name='Id del Rol')
    nombre = models.CharField(max_length=15, verbose_name='Nombre del Rol')

    def __str__(self):
        return self.nombre

class Usuario (models.Model):
    id_Usuario = models.AutoField(primary_key=True, verbose_name='Id del Ususario')
    correo = models.CharField(max_length=50, verbose_name='Correo del Usuario')
    clave = models.CharField(max_length=16, verbose_name='Clave del Usuario')
    estatus = models.CharField(max_length=2, verbose_name='Esta activo o no')
    rut = models.CharField(max_length=11, verbose_name='Rut del usuario')
    rol = models.ForeignKey(Rol,on_delete=models.CASCADE)

    def __str__(self):
        return self.correo
