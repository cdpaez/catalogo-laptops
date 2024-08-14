# forms.py

from django import forms
from .models import Producto, CarritoProducto

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'descripcion']

class CarritoProductoForm(forms.ModelForm):
    class Meta:
        model = CarritoProducto
        fields = ['producto', 'cantidad']
