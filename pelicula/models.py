from django.db import models

# Create your models here.
class Pelicula(models.Model):
    id_pelicula = models.AutoField(primary_key=True)
    titulo_pelicula = models.CharField("Título de la película", max_length=200)
    genero = models.CharField("Género", max_length=100)
    duracion = models.PositiveIntegerField("Duración (minutos)")
    clasificacion = models.CharField("Clasificación", max_length=20)
    sinopsis = models.TextField("Sinopsis", blank=True)

    def __str__(self):
        return self.titulo_pelicula
