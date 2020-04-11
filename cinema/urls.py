from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from peliculas import views

urlpatterns = [
    path('', views.home, name="index"),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('peliculas/', include(('peliculas.urls', 'peliculas'), namespace='peliculas')),
    path('teatros/', include(('teatros.urls', 'teatros'), namespace='teatros')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

admin.site.site_header = "CINEMA Admin"
admin.site.site_title = "CINEMA Admin Portal"
admin.site.index_title = "Bienvenido al portal de CINEMA"
