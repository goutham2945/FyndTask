from django.db import models

class Genre(models.Model):
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name
    

class Movie(models.Model):
    popularity = models.FloatField()
    director = models.CharField(max_length=500)
    genre = models.ManyToManyField(Genre)
    score = models.FloatField()
    name = models.CharField(max_length=500)

    def __str__(self):
        return self.name
