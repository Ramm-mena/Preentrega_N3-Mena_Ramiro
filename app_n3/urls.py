from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name= 'Inicio' ),
    path('Sucursal/', sucursal, name= 'mod1' ),
    path('Empleado/', empleado, name= 'mod2' ),
    path('Vehiculos/', vehiculo, name= 'mod3' ),
    #formulario
    path('vintageclb/', vintageClb, name="form1"),
    #Buscador
    path('buscador/', buscador, name="look1"),
    path('buscador2/', buscador2, name="look2"),


    

]