from django.db import models

# Create your models here.
class Director(models.Model):
    nombre = models.CharField(max_length=200)
    bio = models.TextField()

    def __str__(self) -> str:
        return self.nombre
    
class Pelicula(models.Model):
    titulo = models.CharField(max_length=200)
    director = models.ForeignKey(Director, on_delete=models.CASCADE)
    descripcion = models.TextField()

    def __str__(self):
        return self.titulo