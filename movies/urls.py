from django.urls import path
from . import views

app_name = "movies"

urlpatterns = [
    path('watched', views.watched, name = 'watched'),
    path('', views.index, name = 'index'),
]