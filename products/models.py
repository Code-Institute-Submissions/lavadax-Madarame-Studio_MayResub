from django.db import models

# Create your models here.


class Product(models.Model):
    """
    A class to contain all products
    """
    sku = models.CharField(max_length=254, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=1, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    artist = models.CharField(max_length=254, null=True, blank=True)
    artist_url = models.URLField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.sku
