from django.contrib import admin
from .models import Artist


class ArtistAdmin(admin.ModelAdmin):
    list_display = (
        "artist_name",
        "artist_url",
        "created"
    )

    ordering = ("artist_name",)


admin.site.register(Artist, ArtistAdmin)
