from django.contrib import admin
from .models import Artist


class ArtistAdmin(admin.ModelAdmin):
    list_display = (
        "name",
        "url",
        "created"
    )

    ordering = ("name",)


admin.site.register(Artist, ArtistAdmin)
