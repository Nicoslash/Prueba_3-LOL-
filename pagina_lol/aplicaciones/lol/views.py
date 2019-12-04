from django.shortcuts import render,redirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.generic import View,TemplateView,ListView,UpdateView,CreateView,DeleteView
from django.urls import reverse_lazy
from .models import *
from .forms import *
from .urls import *

from rest_framework import viewsets
from .serializers import *

def home(request):
    posts = Post.objects.filter(estado = True)
    return render(request, 'index.html',{'posts':posts})

def universolol(request):
    return render(request,'universolol.html')

def campeones(request):

    return render(request,'campiones.html')

def novedades(request):
    posts = Post.objects.filter(
        estado = True,
        categoria = Categoria.objects.get(nombre = 'NOTICIAS')
    )
    return render(request,'novedades.html',{'posts':posts})

def listar_noticia(request):
    listado_noticias = Post.objects.all()
    data = {
        'listado_noticias':listado_noticias
    }
    return render(request,'listar_noticias.html',data)

def agregar_noticia(request):
    data = {
        'form':NoticiasForm()
    }

    if request.method == 'POST':
        formulario = NoticiasForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "GUARDADO CORRECTAMENTE"

    return render(request,'agregar_noticia.html',data)

def modificar_noticia(request, id):
    noticia = Post.objects.get(id=id)
    data = {
        'form': NoticiasForm(instance=noticia)
    }

    if request.method == 'POST':
        formulario = NoticiasForm(data=request.POST, instance=noticia)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "MODIFICADO CORRECTAMENTE"
            data['form'] = formulario

    return render(request,'modificar_noticia.html',data)

def eliminar_noticia(request, id):
    noticia = Post.objects.get(id=id)
    noticia.delete()

    return redirect(request,to="listar_noticia")


def login(request):
    return render(request,'login.html')

def detallePost(request,slug):
    post = Post.objects.get(
        slug = slug
    )
    return render(request,'post.html',{'detalle_post':post})

class NoticiaViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = NoticiaSerializer

    
