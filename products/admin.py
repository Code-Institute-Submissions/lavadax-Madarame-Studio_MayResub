from django.contrib import admin
from .models import Product

# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = (
        "sku",
        "price",
        "rating",
        "image",
        "artist",
        "created",
        "updated"
    )

    ordering = ("sku",)


admin.site.register(Product, ProductAdmin)
