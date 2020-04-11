from django.db import models
from peliculas.models import Movie
import datetime

# Modelo Categoria pelicula
class City(models.Model):
    name = models.CharField(max_length=100)

# Modelo Teatros
class Theater(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone = models.IntegerField()
    city = models.ForeignKey(City, null=False, on_delete=models.PROTECT)
    urlimage = models.FileField(null=True,upload_to='teatros/%Y/%m/%d')

# Horario
class Hour(models.Model):
    hour = models.TimeField()

    def __str__(self):
        return str(self.hour)

# Formato
class Format(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

# Sala
class Lounge(models.Model):
    identify = models.IntegerField()
    theater = models.ForeignKey(Theater, null=False, on_delete=models.PROTECT)
    format = models.ManyToManyField(Format)
    seats_number = models.IntegerField()

    def __str__(self):
        #return 'sala:' + str(self.identify) + ' - ' + str(self.theater.name)
        #return 'sala %s - %s' % (self.identify, self.theater.name)
        #return 'sala: {} - {}'.format(self.identify, self.theater.name)
        return f'sala:{self.identify} - {self.theater.name}' #python 3.6 higher

# Funciones
class MovieFunction(models.Model):
    date = models.DateField()
    hour = models.ForeignKey(Hour, null=False, on_delete=models.PROTECT)
    lounge = models.ForeignKey(Lounge, null=False, on_delete=models.PROTECT)
    format = models.ForeignKey(Format, null=False, on_delete=models.PROTECT)
    movie = models.ForeignKey(Movie, null=False, on_delete=models.PROTECT)
    seats_sold = models.IntegerField()

    class Meta:
        unique_together = (("date", "hour", "lounge", "movie"),)

    @property
    def seats_left_to_sell(self):
        seats_number = Lounge.objects.filter(pk=self.lounge)
        return seats_number - self.seats_sold
