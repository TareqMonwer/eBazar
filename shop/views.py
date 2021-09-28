from django.shortcuts import render, get_object_or_404
from shop.models import Category, Product
from cart.forms import CartAddProductForm


def product_list(request, category_slug=None):
    category = None
    products = Product.objects.filter(is_available=True)
    categories = Category.objects.all()
    cart_add_product_form = CartAddProductForm()
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=category)
    ctx = {
        'category': category,
        'categories': categories,
        'products': products,
        'cart_add_product_form': cart_add_product_form,
    }
    return render(request, 'shop/products/list.html', ctx)


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug)
    cart_add_product_form = CartAddProductForm()
    ctx = {'product': product, 'cart_add_product_form': cart_add_product_form}
    return render(request, 'shop/products/detail.html', ctx)
