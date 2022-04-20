"""
Artist models used in database and admin
"""
from django.db import models


class Artist(models.Model):
    """
    A class to contain all artists
    """
    name = models.CharField(max_length=254, null=True, blank=True)
    url = models.URLField(max_length=1024, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
