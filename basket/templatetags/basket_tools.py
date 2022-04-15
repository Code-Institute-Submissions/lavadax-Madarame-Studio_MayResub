from django import template


register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    return price * quantity


@register.filter(name='calc_sizeprice')
def calc_sizeprice(base_price, size):
    size_multi = {
        "A6": 0,
        "A5": 1,
        "A4": 2,
        "A3": 3,
        "A2": 4,
        "A1": 5
        }
    return round(1.1 ** size_multi[size] * float(base_price)) - 0.01
