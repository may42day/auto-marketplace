from django.contrib import admin
from .models import *
from django.db.models import QuerySet

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'user', 'amount', 'price', 'currency', 'on_moderation', 'subcategory', 'category']
    list_editable = ['category', 'on_moderation', 'subcategory']
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
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    search_fields = ['name']

@admin.register(Subcategory)
class SubcategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
    search_fields = ['name', 'category']






