from django.conf import settings
from goods.models import Product
from decimal import Decimal

class Cart(object):

    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart

    def add_to_cart(self, product:Product, amount=1, update_amount=False):
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'quantity':0,
                'price_euro':str(product.price_euro),
                'price_usd':str(product.price_usd),
            }

        if update_amount:
            self.cart[product_id]['amount'] = amount
        else:
            self.cart[product_id]['amount'] += amount
        self.save()


    def remove(self, product:Product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()


    def save(self):
        self.session[settings.CART_SESSION_ID] = self.cart
        self.session.modified = True


    def __iter__(self):
        product_ids = self.cart.keys()
        products = Product.objects.filter(id__in=product_ids)
        for product in products:
            product_id = str(product.id)
            self.cart[product_id]['product'] = product
            self.cart[product_id]['id'] = product_id

        for item in self.cart.values():
            item['price_usd'] = float(item['price_usd'])
            item['price_euro'] = float(item['price_euro'])
            item['total_price_usd'] = round(item['price_usd'] * item['amount'], 2)
            item['total_price_euro'] = round(item['price_euro'] * item['amount'], 2)
            yield item


    def __len__(self):
        return sum(item['amount'] for item in self.cart.values())

    def get_total_price_euro(self):
        total = sum((item['price_euro']) * item['amount'] for item in self.cart.values())
        return round(total, 2)
    def get_total_price_usd(self):
        total = sum(float(item['price_usd']) * item['amount'] for item in self.cart.values())
        return round(total, 2)

    def clear(self):
        del self.session[settings.CART_SESSION_ID]
        self.session.modified = True