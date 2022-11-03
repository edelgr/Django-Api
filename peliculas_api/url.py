from django.urls import path
from . import views

urlpatterns = [
    path('movie-create/', views.movies_create, name='movies-create'),
    path('movie-read/', views.movies_read, name='movies-read'),
    path('movie-read-details/<str:pk>', views.movies_read_details, name='movies-read-details'),
    path('movie-update/<str:pk>', views.movies_update, name='movies-update'),
    path('movie-delete/<str:pk>', views.movies_delete, name='movies-delete'),
]
