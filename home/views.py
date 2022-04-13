"""
Home page views for the madarame_studio project
"""
from django.shortcuts import render

# Create your views here.


def index(request):
    """ A view to return the homepage """
    return render(request, "home/index.html")
