from django.contrib import admin
from .models import Producto,Carrito,Compra,DetalleCompra
#registrar las tablas en el panel de administracion de django

admin.site.register(Producto)
admin.site.register(Carrito)
admin.site.register(Compra)
admin.site.register(DetalleCompra)

