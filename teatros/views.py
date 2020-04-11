from django.urls import reverse_lazy
from django.shortcuts import render
from django.views.generic import ListView
from .models import Theater, MovieFunction

#Listado de películas
class TheaterList(ListView):
    model = Theater

#Listado de Funciones
class MovieFunctionList(ListView):
    template_name = 'peliculas/admin/moviefunction_list.html'
    model = MovieFunction
    paginate_by = 5
