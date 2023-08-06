from django.contrib import admin
from .models import *


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ["pk", "user", "status", "created"]


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ["order", "product", "amount"]
