from django.contrib import admin
from orders.models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product', ]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email', 'phone', 'country',
                    'city', 'postal', 'paid', 'created', 'updated']
    list_filter = ['city', 'country', 'created', 'updated', 'paid']
    inlines = [OrderItemInline]
