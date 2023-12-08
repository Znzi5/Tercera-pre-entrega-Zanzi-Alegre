from django.urls import path
from .views import insertar_datos, buscar_datos

urlpatterns = [
    path('insertar-datos/', insertar_datos, name='insertar_datos'),
    path('buscar-datos/', buscar_datos, name='buscar_datos'),
]
