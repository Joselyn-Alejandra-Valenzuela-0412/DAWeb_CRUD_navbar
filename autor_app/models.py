from django.db import models

# Create your models here.

class Autor(models.Model):
    id_autor=models.CharField(primary_key=True,max_length=6)
    id_edit=models.CharField(max_length=25)
    id_manga=models.CharField(max_length=20)
    nombre=models.CharField(max_length=25)
    apellidos=models.CharField(max_length=20)
    foto=models.ImageField()
    estado=models.CharField(max_length=35)
    nacionalidad=models.CharField(max_length=35)
    num_tel=models.IntegerField()
    correo=models.CharField(max_length=35)
    ciudad=models.CharField(max_length=35)

    def __str__(self):
        return (self).nombre
