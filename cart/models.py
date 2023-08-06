import json
from django.contrib.auth.models import User
from django.db import models

from goods.models import Product


CURRENCY_CHOICES = [
    ("EURO", "Euro"),
    ("USD", "Dollars"),
]

STATUS_CHOICES = [
    ("PLACE", "Placing"),
    ("OPEN", "Open"),
    ("CANCELED", "Canceled"),
    ("DELIVERED", "Delivered"),
]


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(null=True, max_length=40)
    address = models.CharField(null=True, max_length=60)
    postal_code = models.CharField(null=True, max_length=10)
    phone_number = models.CharField(null=True, max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default="PLACE")
    comment = models.CharField(max_length=60, blank=True, null=True)
    currency = models.CharField(max_length=7, choices=CURRENCY_CHOICES, default="Euro")

    def order_cost(self):
        return sum(item.item_cost() for item in self.items.all())

    def status_message(self):
        if self.status == "PLACE":
            return "Fill in additional information to place an order"
        elif self.status == "OPEN":
            return "Awaiting delivery"
        elif self.status == "CANCELED":
            return "The order has been canceled"
        else:
            return "The order has been delivered"

    def get_html_class_for_table(self):
        if self.status == "PLACE":
            return "table-warning"
        elif self.status == "OPEN":
            return "table-light"
        elif self.status == "CANCELED":
            return "table-secondary"
        else:
            return "table-success"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="products", on_delete=models.PROTECT
    )
    amount = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def item_cost(self):
        return self.price * self.amount
