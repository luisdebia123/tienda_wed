from django.shortcuts import render

from .models import Categorias, Post
# Create your views here.


def blog(request):
    posts=Post.objects.all()
    context={'posts': posts}
    return render(request,'app_blog/blog.html', context)

def categorias(request,id):
    categoria=Categorias.objects.get(id=id)
    posts=Post.objects.filter(categorias=categoria)
    context={'posts': posts, 'categoria': categoria}
    return render(request,'app_blog/categorias.html', context)

  