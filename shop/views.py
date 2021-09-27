from django.shortcuts import render, get_object_or_404
from shop.models import Category, Product


def product_list(request, category_slug=None):
    category = None
    products = Product.objects.filter(is_available=True)
    categories = Category.objects.all()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
    return render(request, 'shop/products/list.html', {
        'category': category,
        'categories': categories,
        'products': products
    })


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    return render(request, 'shop/products/detail.html', {'product': product})
