from django.db import models

class Genre(models.Model):
    name= models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.name


class Director(models.Model):
    name= models.CharField(max_length=80, unique=True)

    def __str__(self):
        return self.name

class Movie(models.Model):
    name = models.CharField(max_length=200, unique=True, primary_key=True)
    director = models.ManyToManyField(Director)
    Description = models.TextField(blank=True, null=True)
    genre = models.ManyToManyField(Genre)
    
    def __str__(self):
        return self.name