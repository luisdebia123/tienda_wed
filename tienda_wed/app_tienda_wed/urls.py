from django.urls import path
from .import views

app_name='app_tienda_wed' 



urlpatterns = [    
    path('', views.home, name='home'),

]