from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='movies_index'),
    path('<int:movie_id>', views.detail, name='movies_detail'),
    path('api/movies/', views.api_movies, name='api_movies'),
    path('api/movies/<int:movie_id>',
         views.api_movie_detail, name='api_movie_detail')
]
