from django.urls import path

from autenticacion.views import Registro, cerrar_sesion, logear




urlpatterns = [
    path('', Registro.as_view(), name= 'autenticacion'),
    path('cerrar_sesion', cerrar_sesion, name= 'cerrar'),
    path('logear', logear, name= 'logear'),
]




