from django.contrib import admin
from .models import Producto,Carrito
#registrar las tablas en el panel de administracion de django

admin.site.register(Producto)
admin.site.register(Carrito)

