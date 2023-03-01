from django.urls import path,include
from .views import *

from . import views


urlpatterns = [
    path('CreateFilm/', views.CreateMovie.as_view(),name='create_movie'),
    path('viewAllMovie/', views.ViewallMovie, name="viewwall"),
    path('UpdateMovie/<str:pk>/', views.updateMovie, name="update-movie"),
    path('DeleteMovie/<str:pk>/', views.DeleteMovie, name="update-movie"),
    path('CreateGenre/', views.CreateGenre.as_view(),name='create_movie')
]
