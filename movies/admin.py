from django.contrib import admin
from .models import movie
from import_export.admin import ImportExportModelAdmin
from .resources import MovieResource


class MovieAdmin(ImportExportModelAdmin):
    list_display = ( 'title', 'director', 'actor', 'categoryId', 'imbdUrl', 'coverUrl', 'viewDate', 'timeId', 'priceId', 'description', 'trailer', 'owner')
    list_per_page = 50
    resource_class = MovieResource
    pass

admin.site.register(movie, MovieAdmin)
