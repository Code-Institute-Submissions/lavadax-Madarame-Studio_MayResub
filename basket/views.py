"""
Basket page views for the madarame_studio project
"""
from django.shortcuts import (render, redirect,
                              HttpResponse, get_object_or_404)
from django.contrib import messages
from products.models import Product


def view_basket(request):
    """
    A view that shows the basket page
    """

    return render(request, "basket/basket.html")


def add_to_basket(request, item_id):
    """
    Add a quantity of the specified product to the shopping basket
    """

    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get("quantity"))
    redirect_url = request.POST.get("redirect_url")
    size = request.POST.get("product_size")
    basket = request.session.get("basket", {})

    if item_id in list(basket.keys()):
        if size in basket[item_id]["items_by_size"].keys():
            basket[item_id]["items_by_size"][size] += quantity
            messages.success(request, f'Updated size {size.upper()} \
                {product.sku} quantity to \
                {basket[item_id]["items_by_size"][size]}')
        else:
            basket[item_id]["items_by_size"][size] = quantity
            messages.success(request, f'Added size {size.upper()} \
                {product.sku} to your basket')
    else:
        basket[item_id] = {"items_by_size": {size: quantity}}
        messages.success(request, f'Added size {size.upper()} \
            {product.sku} to your basket')

    request.session["basket"] = basket
    return redirect(redirect_url)


def adjust_basket(request, item_id):
    """
    Adjust the quantity of the specified product to the specified amount
    """
    product = get_object_or_404(Product, pk=item_id)
    quantity = int(request.POST.get("quantity"))
    size = None
    if "product_size" in request.POST:
        size = request.POST["product_size"]
    basket = request.session.get("basket", {})

    if size:
        if quantity > 0:
            basket[item_id]["items_by_size"][size] = quantity
            messages.success(request, f'Updated size {size.upper()} \
                {product.sku} quantity to \
                {basket[item_id]["items_by_size"][size]}')
        else:
            del basket[item_id]["items_by_size"][size]
            if not basket[item_id]["items_by_size"]:
                basket.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} \
                {product.sku} from your basket')
    else:
        if quantity > 0:
            basket[item_id] = quantity
            messages.success(request, f'Updated {product.sku} \
                quantity to {basket[item_id]}')
        else:
            basket.pop(item_id)
            messages.success(request, f'Removed {product.sku} from your bag')

    request.session["basket"] = basket
    template = "basket/basket.html"
    context = {
        "on_basket": True
    }
    return render(request, template, context)


def remove_from_basket(request, item_id):
    """
    Remove the item from the shopping basket
    """
    try:
        product = get_object_or_404(Product, pk=item_id)
        size = None
        if "product_size" in request.POST:
            size = request.POST["product_size"]
        basket = request.session.get("basket", {})

        if size:
            del basket[item_id]["items_by_size"][size]
            if not basket[item_id]["items_by_size"]:
                basket.pop(item_id)
            messages.success(request, f'Removed size {size.upper()} \
                {product.sku} from your basket')
        else:
            basket.pop(item_id)
            messages.success(request, f'Removed {product.sku} \
                from your basket')

        request.session["basket"] = basket
        return HttpResponse(status=200)

    except Exception as error:
        messages.error(request, f'Error removing item: {error}')
        return HttpResponse(status=500)
