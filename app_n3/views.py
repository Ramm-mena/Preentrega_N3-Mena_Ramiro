from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.
#Inicio--------------------------------------------------------
def index(request):
    return render(request, 'app_n3/base.html')
#Modelos-------------------------------------------------------
def sucursal(request):
    ctx= {'sucursales': Sucursal.objects.all()}
    return render(request, 'app_n3/sucursal.html', ctx )
def empleado(request):
    ctx= {'empleados': Empleado.objects.all()}
    return render(request, 'app_n3/empleado.html', ctx )
def vehiculo(request):
    ctx= {'vehiculos': Vehiculo.objects.all()}
    return render(request, 'app_n3/vehiculo.html', ctx )
#Formulario-----------------------------------------------------
def vintageClb(request):
    if request.method == "POST":   
        formulario = vintaje_club(request.POST)
        if formulario.is_valid:
            datos = formulario.cleaned_data
            miembro = Miembro(nombre=datos['nombre'], Apellido=datos['apellido'])
            miembro.save()
            return render(request, "aplicacion/base.html")
    else:
        formulario = vintaje_club()

    return render(request, "app_n3/vintage_club.html" , {"form":formulario})

 #Buscador-------------------------------------------------------
#Buscador-------------------------------------------------------
def buscador(request):
    return render(request ,"app_n3/buscador")
def buscador2(request):
    if request.GET['search']:
        modelo = request.GET['search']
        buscarAuto = Vehiculo.objects.filter(modelo__icontains=modelo)
        return render(request, 
                      "app_n3/resultados_modelo.html", 
                      {"modelo": modelo, "buscarAuto":buscarAuto})
    return HttpResponse("No se ingresaron datos para buscar!")

