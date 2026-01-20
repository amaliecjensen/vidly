from django.urls import path
from . import views
# movies/
# movies/1/details


urlpatterns = [
    path('', views.index, name='index')
]
