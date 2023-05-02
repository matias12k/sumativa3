from django.urls import path
from core.views import listaFormulario
from django.contrib import admin
from django.conf import settings
from django.urls import include
from django.conf.urls.static import static
from core.views import listaFormulario, vista_formulario_mod
from rest_api.viewLogin import login

urlpatterns = [
    path('listaFormulario/', listaFormulario, name= "listaFormulario"),
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('api/', include('rest_api.urls')),

    path('listaFormulario/',listaFormulario, name="listaFormulario"),
    path('datos_formulario/<usuario>',vista_formulario_mod, name="modif_mascota"),
    path('login/', login,name="login"),
]