from django.shortcuts import render, get_object_or_404
from .models import Product
from category.models import Category


def store(request, cat_slug=None):
    categories = None
    products = None

    if cat_slug != None:
        categories = get_object_or_404(Category, cat_slug=cat_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()
    else:
        products = Product.objects.all()
        product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count
    }
    return render(request, 'store/store.html', context)


def product_detail(request, cat_slug, prod_slug):
    try:
        single_product = Product.objects.get(category__cat_slug=cat_slug, product_slug=prod_slug)

    except Exception as e:
        raise e
    context = {
        'single_product': single_product
    }
    return render(request, 'store/product_detail.html', context)
