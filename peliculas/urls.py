from django.urls import path

from .views import ( MoviesList, MoviesListWeek, MoviesCreate, searchMovie,
                     MoviesDetail, load_peliculas, compraBoletasOnline,
                     MoviesListNext )

urlpatterns = [
    path('listar/', MoviesList.as_view(), name='listar'),
    path('listarsemanal/', MoviesListWeek.as_view(), name='listarsemanal'),
    path('listarestrenos/', MoviesListNext.as_view(), name='listarestrenos'),
    path('crear/', MoviesCreate.as_view(), name='crear'),
    path('detalle/<int:pk>/', MoviesDetail.as_view(), name='detalle'),
    path('buscar/', searchMovie, name='buscar'),
    path('compraboletasonline', compraBoletasOnline, name="compraboletasonline"),
    #AJAX
    path('ajax/load-peliculas/', load_peliculas, name='ajax_load_peliculas'),
]
