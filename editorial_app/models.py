from django.db import models

# Create your models here.

class Editorial(models.Model):
    id_edit=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=100)
    pais=models.CharField(max_length=25)
    anio_fundac=models.DateField()
    fundador=models.CharField(max_length=50)
    correo=models.CharField(max_length=80)
    proyectos=models.CharField(max_length=150)

    def __str__(self):
        return (self).nombre
