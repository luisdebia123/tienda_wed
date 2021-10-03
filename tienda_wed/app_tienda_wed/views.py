from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    return render(request,'app_tienda_wed/home.html')


def tienda(request):
    return render(request,'app_tienda_wed/tienda.html')



def contacto(request):
    return render(request,'app_tienda_wed/contacto.html')