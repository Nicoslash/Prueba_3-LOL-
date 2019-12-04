from django.urls import path
from .views import *

urlpatterns = [
    path('',home, name = 'index'),
    path('universolol/',universolol, name = 'universolol'),
    path('campeones/',campeones, name = 'campeones'),
    path('novedades/',novedades, name = 'novedades'),
    path('login/',login, name = 'login'),
    path('listar_noticias/',listar_noticia, name = 'listar_noticias'),
    path('agregar_noticia/',agregar_noticia, name = 'agregar_noticia'),
    path('modificar_noticia/<id>/',modificar_noticia, name = 'modificar_noticia'),
    path('eliminar_noticia/<id>/',eliminar_noticia, name = 'eliminar_noticia'),

    path('<slug:slug>/',detallePost, name = 'detalle_post'),
]
