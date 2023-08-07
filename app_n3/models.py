from django.db import models

# Create your models here.


class Sucursal(models.Model):
    localidad= models.CharField(max_length=50)
    calle= models.CharField(max_length=50)
    numeracion= models.IntegerField()
    def __str__(self):
        return f'{self.localidad}'
class Empleado(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    puesto= models.CharField(max_length=50)
    Email= models.EmailField()
    def __str__(self):
        return f'{self.apellido}, {self.nombre}'
class Vehiculo(models.Model):
    marca= models.CharField(max_length=50)
    modelo= models.CharField(max_length=50)
    anio= models.IntegerField()
    color= models.CharField(max_length=50)
    def __str__(self):
        return f'{self.marca}, {self.modelo}'
class Miembro(models.Model):
    nombre= models.CharField(max_length=50)
    apellido= models.CharField(max_length=50)
    Email= models.EmailField()