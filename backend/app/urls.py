from django.urls import path,include
from .views import *

from . import views


urlpatterns = [
    path('CreateFilm/', views.CreateMovie.as_view(),name='create_movie'),
    path('viewAllMovie/', views.ViewallMovie, name="viewwall"),
    path('CreateGenre/', views.CreateGenre.as_view(),name='create_movie'),
]