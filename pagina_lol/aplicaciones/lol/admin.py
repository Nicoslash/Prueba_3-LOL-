from django.contrib import admin
from .models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

class CategoriaResource(resources.ModelResource):
    class Meta:
        model = Categoria

class CategoriaAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['nombre']
    list_display = ('nombre','estado','fecha_creacion',)
    resource_class = CategoriaResource

class AutorResoruce(resources.ModelResource):
    class Meta:
        model = Autor

class AutorAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['apellidos','nombres','correo']
    list_display = ('nombres','apellidos', 'correo', 'estado', 'fecha_creacion',)
    resource_class = AutorResoruce

class PostResource(resources.ModelResource):
    class Meta:
        model = Post

class PostAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    search_fields = ['titulo']
    list_display = ('titulo','categoria','fecha_creacion', 'estado', 'autor')
    resource_class = PostResource

admin.site.register(Categoria,CategoriaAdmin)
admin.site.register(Autor,AutorAdmin)
admin.site.register(Post,PostAdmin)
