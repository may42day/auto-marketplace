from django.contrib import admin
from .models import Category, Product
from django.db.models import  QuerySet

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'owner', 'amount', 'price', 'currency', 'on_moderation', 'stock_value']
    list_editable = ['category', 'on_moderation']
    ordering = ['category', 'owner', 'on_moderation']
    actions = ['set_moderation_approval']
    list_per_page = 20
    search_fields = ['name']


    @admin.display(description='Stock value')
    def stock_value(self, product: Product):
        return product.amount * product.price

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



