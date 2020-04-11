from django.urls import path

from .views import TheaterList, MovieFunctionList

urlpatterns = [
    path('listar/', TheaterList.as_view(), name='listar'),
    path('listarfunciones/', MovieFunctionList.as_view(), name='listarfunciones'),
]
