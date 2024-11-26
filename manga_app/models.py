from django.db import models

# Create your models here.

class Manga(models.Model):
    id_manga=models.CharField(primary_key=True,max_length=6)
    titulo=models.CharField(max_length=100)
    volumen=models.IntegerField()
    genero=models.CharField(max_length=25)
    sinopsis=models.CharField(max_length=100)
    fecha_publ=models.DateField()
    precio=models.IntegerField()

    def __str__(self):
        return (self).titulo