from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from .models import Movie
from teatros.models import MovieFunction, Hour
import datetime
#AJAX
from django.urls import reverse_lazy, reverse
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.core import serializers

#Página principal
def home(request):
    '''Variables para el buscador de películas'''
    movie = Movie.objects.filter(movie_week=True)
    #selección de las primeras 7 fechas disponibles a partir del día actul
    dates = (MovieFunction.objects.values('date')
                                  .distinct()
                                  .filter(date__range=(datetime.datetime.today(),
                                                       datetime.datetime.today()+datetime.timedelta(days=7))))
    hour = Hour.objects.all()
    context = {"movies": movie, "dates": dates, "hours": hour}

    return render(request, 'home.html', context)

#Listado de películas en cartelera semanal
class MoviesListNext(ListView):

    def get_queryset(self):
        queryset = Movie.objects.filter(next_week=True)
        return queryset

#Listado de películas en cartelera semanal
class MoviesListWeek(ListView):

    def get_queryset(self):
        queryset = Movie.objects.filter(movie_week=True)
        return queryset

#Listado de películas ( para el administrador )
class MoviesList(ListView):
    template_name = 'peliculas/admin/movie_list.html'
    context_object_name = 'movies'
    model = Movie

#Crear Películar
class MoviesCreate(CreateView):
    model = Movie
    success_url = reverse_lazy('pelicular:listar')
    fields = '__all__'

#Detalle de película
class MoviesDetail(DetailView):
    model = Movie

    def get_context_data(self, **kwargs):
        kwargs['cast'] = self.get_object().cast.all()
        return super(MoviesDetail, self).get_context_data(**kwargs)

#Búsqueda de péliculas
def searchMovie(request):
    if request.method == 'POST':
        pattern = request.POST['search']
        movie = Movie.objects.filter(movie_week=True, name__contains=pattern)
    else:
        movie = Movie.objects.filter(movie_week=True)
    return render(request, 'peliculas/movie_search.html', {'object_list':movie, 'search':pattern})

#Compra de boletas online, desde el banner del home
def compraBoletasOnline(request):
    if request.method == 'POST':
        movie = Movie.objects.get(pk=request.POST['movie'])
    else:
        movie = 0
    return render(request, 'tiquetes/compra_form.html', {'movie':movie})


######________________ AJAX  ________________#######
def load_peliculas(request):
    moviefunction = MovieFunction.objects.filter(date=request.GET.get('date'))
    mv = []
    for m in moviefunction:
        mv.append(m.movie.id)
    movie = Movie.objects.filter(id__in=mv, movie_week=True)
    data = serializers.serialize('json', list(movie))
    return HttpResponse(data, content_type="application/json")
