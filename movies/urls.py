from django.urls import URLPattern, path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('', views.MoviesHandler.as_view()),
    path('search/genre/<str:pk>/', views.GetGenreMovies.as_view()),
    path('search/director/<str:pk>/', views.GetDirectorMovies.as_view()),
    path('search/Title/<str:pk>/', views.GetTitleMovies.as_view()),
    path('comments/<str:pk>/', views.GetComment.as_view()),
    path('getGenres/', views.GetGenres.as_view()),
    path('getDirectors', views.GetDirectors.as_view()),
    path('comment/', views.MakeComment.as_view()),
    path('like/', views.MakeLike.as_view()),
    path('comments/<str:pk>/', views.GetMovieComments.as_view()),
    path('<str:pk>/', views.MovieHandler.as_view()),
]