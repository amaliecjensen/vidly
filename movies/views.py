from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, get_object_or_404
from .models import Movie


def index(request):
    movies = Movie.objects.all()
    return render(request, 'movies/index.html', {'movies': movies})


def detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    return render(request, 'movies/detail.html', {'movie': movie})


def api_movies(request):
    movies = list(Movie.objects.all().values())
    return JsonResponse({'movies': movies})


def api_movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    data = {
        'title': movie.title,
        'release_year': movie.release_year,
        'number_in_stock': movie.number_in_stock,
        'daily_rate': movie.daily_rate,
        'genre': movie.genre.name
    }
    return JsonResponse(data)
