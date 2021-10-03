from django.shortcuts import render, redirect

from .forms import Form_Contacto
from django.core.mail import EmailMessage 
from django.contrib import messages
# Create your views here.


def contacto(request):
    form_contacto = Form_Contacto()
    if request.method=='POST':
        form_contacto=Form_Contacto(data=request.POST)
        if form_contacto.is_valid():
            print(form_contacto)
            nombre=request.POST.get("nombre")
            email=request.POST.get("email")
            contenido=request.POST.get("contenido")

            email=EmailMessage("Mensaje desde tienda wed",
            "El usuario con nombre {} con la dirección{} escribe lo siguiente:\n\{}"
            .format(nombre, email, contenido),"",["djangopython75@gmail.com"],reply_to=[email])
            
            messages.success(request, f"Información enviada correctamente")


        try:
            email.send()
            return redirect('app_contacto:contacto' )
        except:
            return redirect('app_contacto:contacto' )

    context={'form_contacto': form_contacto}
    return render(request,'app_contacto/contacto.html', context)
