"""
Home page views for the madarame_studio project
"""
from django.shortcuts import render
from products.models import Product

# Create your views here.


def index(request):
    """ A view to return the homepage """

    products = Product.objects.all()
    query = None
    sort = "created"
    direction = "desc"
    sortkey = f"-{sort}"
    limit = 4
    current_sorting = f"{sort}_{direction}"

    products = products.order_by(sortkey)[:limit]
    context = {
        "products": products,
        "query": query,
        "sorting": current_sorting,
    }
    return render(request, "home/index.html", context)
