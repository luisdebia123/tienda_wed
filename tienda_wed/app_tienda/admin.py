from django.contrib import admin

from .models import Categoria, Producto

# Register your models here.

class TiendaAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class ProductoAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Categoria, TiendaAdmin)
admin.site.register(Producto, TiendaAdmin)