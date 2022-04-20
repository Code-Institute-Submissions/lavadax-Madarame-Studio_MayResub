"""
Home page urls for the madarame_studio project
"""
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home"),
]
