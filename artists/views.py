from django.shortcuts import render, get_object_or_404
from .models import Artist


def artist_detail(request, artist_id):
    """ A view to show individual artist details """

    artist = get_object_or_404(Artist, pk=artist_id)
    products = artist.products.all()

    context = {
        "artist": artist,
        "products": products,
    }

    return render(request, "artists/artist_detail.html", context)
