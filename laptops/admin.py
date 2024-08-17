from django.contrib import admin
from .models import cliente_Tienda, producto_Tienda
#registrar las tablas en el panel de administracion de django

admin.site.register(cliente_Tienda)
admin.site.register(producto_Tienda)
