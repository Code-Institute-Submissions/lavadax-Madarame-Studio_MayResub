"""
Admin settings for Product objects for the madarame_studio project
"""
from django.contrib import admin
from .models import Product


class ProductAdmin(admin.ModelAdmin):
    """
    Admin settings for Product objects for the madarame_studio project
    """
    list_display = (
        "sku",
        "base_price",
        "rating",
        "image",
        "artist",
        "created",
        "updated"
    )

    ordering = ("sku",)


admin.site.register(Product, ProductAdmin)
