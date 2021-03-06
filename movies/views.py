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


class GetMovieComments(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get_comments(self, pk):
        movie = Movie.objects.get(name=pk)
        comments = Comment.objects.filter(movie=movie)
        try:
            return comments
        except Movie.DoesNotExist:
            raise Http404
    def get(self, request, pk, format=None):
        comments = self.get_comments(pk)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)


class GetComment(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def get(self, requeset, pk, format=None):
        comment = Comment.objects.get(id=pk)
        serializer = CommentSerializer(comment, many=False)
        return Response(serializer.data)


class MakeComment(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, format=None):
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MakeLike(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, format=False):
        serializer = LikeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class GetGenres(APIView):
    permission_classes = []
    def get(self, request, format=False):
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response (serializer.data)


class GetDirectors(APIView):
    permission_classes = []
    def get(self, request, format=False):
        directors = Director.objects.all()
        serializer = DirectorSerializer(directors, many=True).data
        return Response (serializer.data)