# forms.py

from django import forms
from .models import Producto, Carrito

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'descripcion']

class CarritoProductoForm(forms.ModelForm):
    class Meta:
        model = Carrito
        fields = ['producto', 'cantidad']
