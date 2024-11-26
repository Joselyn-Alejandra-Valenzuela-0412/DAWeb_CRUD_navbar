from django.db import models

# Create your models here.

class Venta(models.Model):
    id_venta=models.CharField(primary_key=True,max_length=6)
    id_manga=models.CharField(max_length=100)
    id_emp=models.CharField(max_length=25)
    id_cliente=models.CharField(max_length=25)
    cantidad=models.IntegerField()
    total=models.PositiveIntegerField()
    fecha_venta=models.DateField()

    def __str__(self):
        return (self).id_venta