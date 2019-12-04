from django import forms
from django.forms import ModelForm
from .models import *

class NoticiasForm(ModelForm):

    class Meta:
        model = Post
        fields = ['titulo','slug','descripcion','contenido','imagen','autor','categoria','estado']
