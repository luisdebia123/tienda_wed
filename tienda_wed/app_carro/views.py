from django.shortcuts import render
from django.shortcuts import redirect
from .carro import Carro

from app_tienda.models import Producto


# Create your views here.

def agregar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.agregar(producto=producto)
    return redirect('app_tienda:tienda')

def eliminar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.eliminar(producto=producto)
    return redirect('app_tienda:tienda')

def restar_producto(request, producto_id):
    carro = Carro(request)
    producto = Producto.objects.get(id=producto_id)
    carro.restar_producto(producto=producto)
    return redirect('app_tienda:tienda')

def limpiar_carro(request, producto_id):
    carro = Carro(request)
    carro.limpiar_carro()
    return redirect('app_tienda:tienda')

