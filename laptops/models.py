from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class cliente_Tienda (models.Model):
    id_cliente = models.AutoField(primary_key=True)
    nombre_cliente = models.CharField(max_length=100)
    apellido_cliente = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.id_cliente} {self.nombre_cliente} {self.apellido_cliente}"

class producto_Tienda (models.Model):
    id_producto = models.AutoField(primary_key=True)
    nombre_producto = models.CharField(max_length=100)
    precio_producto = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True)
    def __str__(self):
        return f"{self.id_producto} {self.nombre_producto}"