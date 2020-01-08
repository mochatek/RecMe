from django.db import models
from movies.models import Movie, Watched
from django.contrib.auth.models import User

class Recommend(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    strength = models.FloatField()