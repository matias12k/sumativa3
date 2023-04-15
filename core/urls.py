from django.urls import path
from .views import home, accion, terror, estrategia, deporte, registro, inicio_sesion


urlpatterns = [
    path('',home, name="inicio"),
    path('accion/',accion, name="accion"),
    path('terror/',terror, name='terror'),
    path('estrategia/',estrategia, name='estrategia'),
    path('deporte/', deporte, name='deporte'),
    path('registro/', registro, name='registro'),
    path('inicio_sesion/', inicio_sesion, name='inicio_sesion')

]