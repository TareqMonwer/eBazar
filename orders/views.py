from django.shortcuts import render
from orders.models import OrderItem
from orders.forms import OrderCreateForm
from cart.cart import Cart


def create_order(request):
    cart = Cart(request)
    if len(cart) < 1:
        return render(request, 'orders/empty_cart_warning.html')
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    product=item['product'],
                    order=order,
                    price=item['price'],
                    quantity=item['quantity'],
                )
            cart.clear()
            return render(request, 'orders/created.html', {'order': order})
    else:
        form = OrderCreateForm()
    return render(request, 'orders/create.html', {'form': form, 'cart': cart})
