from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import Director, Pelicula

def lista_directores(request):
    directores = Director.objects.all()
    return render(request, 'director/lista_directores.html', {'directores': directores})

def detalle_director(request, director_id):
    director = Director.objects.get(id=director_id)
    peliculas = Pelicula.objects.filter(director=director)
    return render(request, 'director/detalle_director.html', {'director': director, 'peliculas': peliculas})

def detalle_pelicula(request, pelicula_id):
    pelicula = Pelicula.objects.get(id=pelicula_id)
    return render(request, 'director/detalle_pelicula.html', {'pelicula': pelicula})
