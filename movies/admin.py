from django.contrib import admin
from .models import Movie, Watched
from import_export.admin import ImportExportModelAdmin
# Register your models here.

admin.site.register(Watched)
@admin.register(Movie)
class MovieAdmin(ImportExportModelAdmin):
    pass