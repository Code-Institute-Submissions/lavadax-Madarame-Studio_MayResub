"""
Admin settings for Order objects for the madarame_studio project
"""
from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    """
    Specify display settings in admin view for OrderLineItem model
    """
    model = OrderLineItem
    readonly_fields = ("lineitem_total",)


class OrderAdmin(admin.ModelAdmin):
    """
    Specify display settings in admin view for Order model
    """
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = ("order_number", "date", "delivery_cost",
                       "order_total", "grand_total", "original_basket",
                       "stripe_pid")

    fields = ("order_number", "user_profile", "date", "full_name",
              "email", "phone_number", "address_line_1", "address_line_2",
              "town_city", "county_state", "zip_code", "country",
              "delivery_cost", "order_total", "grand_total",
              "original_basket", "stripe_pid")

    list_display = ("order_number", "date", "full_name",
                    "order_total", "delivery_cost", "grand_total")

    ordering = ("-date",)


admin.site.register(Order, OrderAdmin)
