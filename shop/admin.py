from django.contrib import admin
from shop.models import Category, Product

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug']
    prepopulated_fields = {'slug': ('name',)}

@admin.register(Product)
class ProdcuctionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'slug', 'price', 'sale_price', 'is_available']
    list_display_links = ['id', 'name', 'slug']
    prepopulated_fields = {'slug': ('name',)}