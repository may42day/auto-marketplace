from django.contrib import admin
from .models import Category, Product, ShoppingCart
from django.db.models import  QuerySet

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'user', 'amount', 'price', 'currency', 'on_moderation']
    list_editable = ['category', 'on_moderation']
    ordering = ['category', 'user', 'on_moderation']
    actions = ['set_moderation_approval']
    list_per_page = 20
    search_fields = ['name']


    @admin.action(description='Approve moderation')
    def set_moderation_approval(self, request, qs:QuerySet):
        update_counter = qs.update(on_moderation = False)
        self.message_user(
            request,
            f'{update_counter} entries were updated')

@admin.register(Category)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    search_fields = ['name']

@admin.register(ShoppingCart)
class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'amount', 'total_price']


    @admin.display(description='Total Price')
    def total_price(self, cart: ShoppingCart):
        total = cart.amount * cart.product.price
        currency = cart.product.currency
        return f'{total} {currency}'



