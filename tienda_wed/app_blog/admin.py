from django.contrib import admin

from .models import Post, Categorias

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

class CategoriasAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Post, BlogAdmin)
admin.site.register(Categorias, CategoriasAdmin)

