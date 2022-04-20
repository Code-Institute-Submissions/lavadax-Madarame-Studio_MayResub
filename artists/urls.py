"""
artist urls for the madarame_studio project
"""
from django.urls import path
from . import views

urlpatterns = [
    path('<int:artist_id>/', views.artist_detail, name='artist_detail'),
]
