from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    movie = models.CharField(max_length = 60)
    year = models.IntegerField()
    language = models.CharField(max_length = 20)
    action = models.IntegerField()
    adventure = models.IntegerField()
    anthology = models.IntegerField()
    biographical = models.IntegerField()
    biopic = models.IntegerField()
    campus = models.IntegerField()
    children = models.IntegerField()
    comedy = models.IntegerField()
    crime = models.IntegerField()
    drama = models.IntegerField()
    family = models.IntegerField()
    fantasy = models.IntegerField()
    heist = models.IntegerField()
    historical = models.IntegerField()
    horror = models.IntegerField()
    masala = models.IntegerField()
    music = models.IntegerField()
    mystery = models.IntegerField()
    patriotism = models.IntegerField()
    period = models.IntegerField()
    political = models.IntegerField()
    psychological = models.IntegerField()
    revenge = models.IntegerField()
    road = models.IntegerField()
    romantic = models.IntegerField()
    satire = models.IntegerField()
    social = models.IntegerField()
    sport = models.IntegerField()
    suspense = models.IntegerField()
    thriller = models.IntegerField()

    def __str__(self):
        return self.movie


class Watched(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    rating = models.FloatField()