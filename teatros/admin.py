from django.contrib import admin

from .models import City, Theater, Hour, Format, Lounge, MovieFunction

# Register your models here.
admin.site.register(City)
admin.site.register(Theater)
admin.site.register(Hour)
admin.site.register(Format)
admin.site.register(Lounge)
admin.site.register(MovieFunction)
