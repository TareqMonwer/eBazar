from django.urls import path
from shop.views import (product_list, product_detail)

app_name = 'shop'
urlpatterns = [
    path('', product_list, name='products'),
    path('<slug:category_slug>/', product_list, name='category_products'),
    path('<int:id>/<slug:slug>/', product_detail, name='detail'),
]
