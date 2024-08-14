from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError 


from django.contrib.auth.decorators import login_required
from .models import Carrito, Producto


from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')
def registro(request):
    if request.method == 'GET':
        print('enviando formulario')
        return render(request, 'registro.html', {
            'form': UserCreationForm
        })
    else:
        print(request.POST)
        if request.POST['password1'] == request.POST['password2']:
            try:
                #registrat usuario
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password2'])
                user.save()
                login(request,user)
                return redirect('catalogo')
            except IntegrityError:
                return render(request, 'registro.html', {
                    'form': UserCreationForm,
                    'error': 'Ya existe ese usuario'
                })
            
        return render(request, 'registro.html', {
            'form': UserCreationForm,
            'error': 'las contrasenas no coinciden'
        })
    
def catalogo(request):
    return render(request,'catalogo.html')

def salir(request):
    logout(request)
    return redirect('home')
def inicio(request):
    if request.method == 'GET':
        return render(request,'inicio.html',{
            'form': AuthenticationForm
        })
    else:
        print(request.POST)
        user=authenticate(request, username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'inicio.html',{
                'form': AuthenticationForm,
                'error': 'Usuario o contrasena incorrect@'
            })
        else:
            login(request,user)
            return redirect('catalogo')

#carrito
@login_required
def carrito(request):
    carrito_items = Carrito.objects.filter(usuario=request.user)
    
    # Calcular el total para cada producto en el carrito y el total general
    for item in carrito_items:
        item.total = item.cantidad * item.producto.precio
    
    total_general = sum(item.total for item in carrito_items)
    
    return render(request, 'carrito.html', {'carrito_items': carrito_items, 'total_general': total_general})



@login_required
def agregar_al_carrito(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        
        # Verificar si el producto ya está en la base de datos
        producto, creado = Producto.objects.get_or_create(nombre=nombre, defaults={'precio': precio})
        
        # Agregar el producto al carrito
        carrito_item, creado = Carrito.objects.get_or_create(usuario=request.user, producto=producto, defaults={'cantidad': 1})
        
        if not creado:
            # Si el producto ya estaba en el carrito, incrementar la cantidad
            carrito_item.cantidad += 1
            carrito_item.save()
        
        return redirect('catalogo')  # Redirigir a la página de catálogo o a donde quieras
