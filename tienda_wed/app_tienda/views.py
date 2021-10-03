from django.shortcuts import render

from .models import Categoria, Producto
# Create your views here.


def tienda(request):
    productos = Producto.objects.all()
    context = {'productos': productos}
    return render(request,'app_tienda/tienda.html', context)
