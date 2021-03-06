from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def basket_contents(request):

    basket_items = []
    total = 0
    product_count = 0
    basket = request.session.get("basket", {})
    size_multi = {
        "A6": 0,
        "A5": 1,
        "A4": 2,
        "A3": 3,
        "A2": 4,
        "A1": 5
        }

    for item_id, item_data in basket.items():
        if isinstance(item_data, int):
            product = get_object_or_404(Product, pk=item_id)
            total += item_data * product.base_price
            product_count += item_data
            basket_items.append({
                "item_id": item_id,
                "quantity": item_data,
                "product": product,
            })
        else:
            product = get_object_or_404(Product, pk=item_id)
            for size, quantity in item_data["items_by_size"].items():
                total += quantity * (round(1.1 ** size_multi[size] * float(
                        product.base_price)) - 0.01)
                product_count += quantity
                basket_items.append({
                    "item_id": item_id,
                    "quantity": quantity,
                    "product": product,
                    "size": size,
                })

    delivery = total * (settings.STANDARD_DELIVERY_PERCENTAGE / 100)

    grand_total = delivery + total

    context = {
        "basket_items": basket_items,
        "total": total,
        "product_count": product_count,
        "delivery": delivery,
        "grand_total": grand_total,
    }
    return context
