"""
Admin settings for Artist objects for the madarame_studio project
"""
from django.contrib import admin
from .models import Artist


class ArtistAdmin(admin.ModelAdmin):
    """
    Specify display settings in admin view for Artist model
    """
    list_display = (
        "name",
        "url",
        "created"
    )

    ordering = ("name",)


admin.site.register(Artist, ArtistAdmin)
