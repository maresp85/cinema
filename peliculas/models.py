from django.db import models
import datetime

# Modelo Categoria pelicula
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

''' Una película puede tener muchos actores y
    los actores pueden tener muchas películas '''
class Cast(models.Model):
    name = models.CharField(max_length=100)

# Modelo Peliculas
class Movie(models.Model):
    name = models.CharField(max_length=100)
    director = models.CharField(max_length=100)
    rating = models.CharField(max_length=4)
    runtime = models.IntegerField()
    synopsis = models.CharField(max_length=800)
    release_date = models.DateField(default=datetime.datetime.now())
    movie_week = models.BooleanField(default=True)
    next_week = models.BooleanField(default=False)
    category = models.ForeignKey(Category, null=False, on_delete=models.PROTECT)
    urlimage = models.FileField(null=True,upload_to='peliculas/%Y/%m/%d')
    videointro = models.CharField(max_length=400, null=True)
    cast = models.ManyToManyField(Cast)

    def __str__(self):
        return self.name
