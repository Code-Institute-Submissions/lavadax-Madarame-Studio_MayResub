from django.db import models


class Artist(models.Model):
    """
    A class to contain all artists
    """
    artist_name = models.CharField(max_length=254, null=True, blank=True)
    artist_url = models.URLField(max_length=1024, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.artist_name
