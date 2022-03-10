from django.db import models
import uuid
from users.models import User

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


class Comment(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, editable=False, primary_key=True)
    title = models.CharField(max_length=200)
    body = models.TextField(null=True, blank=True)
    reply = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)


class Like(models.Model):
    vote = models.BooleanField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)