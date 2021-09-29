from django.db import models
from shop.models import Product


class Order(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=15)
    address = models.CharField(max_length=255)
    country = models.CharField(max_length=100)
    city = models.CharField(max_length=255)
    postal = models.CharField('Zip/postal Code', max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created',)

    def __str__(self) -> str:
        return f'Order {self.id}'

    def get_total_cost(self) -> int:
        return sum(item.get_cost() for item in self.items.all())


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, 
        on_delete=models.CASCADE, related_name='order_items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self) -> str:
        return str(self.id)

    def get_cost(self) -> int:
        return self.price * self.quantity
