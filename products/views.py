from django.shortcuts import render
from products.models import ProductCategory, Product
# Create your views here.
def index(req):
    context = {
        'title': 'Stooooore',
        'username': 'User',
        'is_promotion': True,
    }
    return render(req, 'products/index.html', context)

def products(req):
    context = {
        'title': 'Catalog',
        'products': Product.objects.all(),
        'categories': ProductCategory.objects.all(),

    }
    return render(req, 'products/products.html', context)