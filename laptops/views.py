from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import clienteForm, productoForm
from .models import cliente_Tienda,producto_Tienda



#registro de usuario
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
            return redirect('dashboard')
       
def salir(request):
    logout(request)
    return redirect('home')

def dashboard(request):
    if request.method == 'POST':
        if 'client-form' in request.POST:
            form_client = clienteForm(request.POST)
            if form_client.is_valid():
                form_client.save()
                return redirect('dashboard')
        elif 'product-form' in request.POST:
            form_product = productoForm(request.POST, request.FILES)
            if form_product.is_valid():
                form_product.save()
                return redirect('dashboard')
    else:
        form_client = clienteForm()
        form_product = productoForm()

    clientes = cliente_Tienda.objects.all()
    productos = producto_Tienda.objects.all()

    contexto = {
        'clientes': clientes,
        'productos':productos,
        'form_client': form_client,
        'form_product': form_product,
    }

        
    return render (request, 'dashboard.html',contexto)
