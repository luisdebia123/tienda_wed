from django.shortcuts import render

from .models import Servicio
# Create your views here.


def servicios(request):
    servicios = Servicio.objects.all()
    context = {'servicios': servicios}
    return render(request,'app_servicios/servicios.html', context)