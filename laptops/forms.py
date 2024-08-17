# forms.py

from django import forms
from .models import cliente_Tienda, producto_Tienda

class clienteForm(forms.ModelForm):
    class Meta:
        model = cliente_Tienda
        fields = ['nombre_cliente', 'apellido_cliente']

class productoForm(forms.ModelForm):
    class Meta:
        model = producto_Tienda
        fields = ['nombre_producto', 'precio_producto', 'imagen']