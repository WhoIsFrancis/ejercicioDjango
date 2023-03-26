from django.contrib import admin
from .models import Director, Pelicula

# Register your models here.
admin.site.site_header = 'Administración de CineApp'
admin.site.site_title = 'CineApp'
admin.site.index_title = 'Panel de control'

class PeliculaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'director', 'descripcion')

class DirectorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'bio')


admin.site.register(Director, DirectorAdmin)
admin.site.register(Pelicula, PeliculaAdmin)

