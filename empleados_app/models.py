from django.db import models

# Create your models here.

class Empleado(models.Model):
    id_emp=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=25)
    apellidos=models.CharField(max_length=25)
    direccion=models.CharField(max_length=80)
    telefono=models.IntegerField()
    area_gen=models.CharField(max_length=25)
    sueldo=models.PositiveIntegerField()

    def __str__(self):
        return (self).nombre