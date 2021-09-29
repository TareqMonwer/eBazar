from django.conf import settings
from shop.models import Product


class RecentlyVisitedProducts():
    def __init__(self, request) -> None:
        self.session = request.session
        recently_visited_products = request.session.get(
            settings.RECENT_PRODUCTS_SESSION_KEY)
        if not recently_visited_products:
            recently_visited_products = self.session[settings.RECENT_PRODUCTS_SESSION_KEY] = {
            }
        self.recently_visited_products = recently_visited_products

    def __iter__(self) -> None:
        product_ids = self.recently_visited_products.keys()
        products = Product.objects.filter(id__in=product_ids)
        recently_visited_products = self.recently_visited_products.copy()

        for product in products:
            recently_visited_products[str(product.id)] = product
        
        for item in recently_visited_products.values():
            yield item
    
    def add(self, product_id) -> None:
        product_id = str(product_id)
        if product_id not in self.recently_visited_products:
            self.recently_visited_products[product_id] = {product_id: product_id}
        self.session.modified = True

