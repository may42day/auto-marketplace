from django.contrib import admin
from .cart import Cart


# @admin.register(Cart)
# class ShoppingCartAdmin(admin.ModelAdmin):
#     list_display = ['user', 'product', 'amount', 'total_price']
#
#
#     @admin.display(description='Total Price')
#     def total_price(self, cart: Cart):
#         total = cart.amount * cart.product.price
#         currency = cart.product.currency
#         return f'{total} {currency}'