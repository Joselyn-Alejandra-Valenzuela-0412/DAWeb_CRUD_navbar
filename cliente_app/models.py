from django.db import models

# Create your models here.

class Cliente(models.Model):
    id_cliente=models.CharField(primary_key=True,max_length=6)
    nombre=models.CharField(max_length=25)
    apellidos=models.CharField(max_length=35)
    prod_adqu=models.CharField(max_length=100)
    tipo_pago=models.CharField(max_length=20)
    num_tel=models.IntegerField()
    total_compra=models.IntegerField()

    def __str__(self):
        return (self).nombre
