from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *
from rest_framework import status
from django.http import Http404


class MoviesHandler(APIView):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    def get(self, request, format=None):
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovieHandler(APIView):
    permission_classes = [permissions.IsAdminUser, permissions.IsAuthenticated]
    def _get_movie(self, pk):
        try:
            return Movie.objects.get(name=pk)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        movie = self._get_movie(pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        movie = self._get_movie(pk)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        movie = self._get_movie(pk)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class GetGenreMovies(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get_movies(self, pk):
        genre = Genre.objects.get(name=pk)
        movies = Movie.objects.filter(genre=genre)
        try:
            return movies
        except Genre.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        movies = self.get_movies(pk)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)

class GetDirectorMovies(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get_movies(self, pk):
        director = Director.objects.get(name=pk)
        movies = Movie.objects.filter(director=director)
        try:
            return movies
        except Genre.DoesNotExist:
            raise Http404
    
    def get(self, request, pk, format=None):
        movies = self.get_movies(pk)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


class GetTitleMovies(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get_movies(self, pk):
        movies = Movie.objects.filter(name__contains=pk)
        try:
            return movies
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        movies = self.get_movies(pk)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)