import json
from django.contrib.auth.models import User
from django.db import models
from django.contrib.postgres.fields import ArrayField

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(null=True, max_length=40)
    address = models.CharField(null=True, max_length=60)
    postal_code = models.CharField(null=True, max_length=10)
    phone_number = models.CharField(null=True, max_length=10)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    STATUS_CHOICES = [
        ('OPEN', 'Open'),
        ('CANCELED', 'Canceled'),
        ('DELIVERED', 'Delivered'),
    ]
    status = models.CharField(max_length=9, choices=STATUS_CHOICES, default='OPEN')
    comment = models.CharField(max_length=60, blank=True, null=True)
    total_sum = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    order_info = models.CharField(max_length=300, blank=True, null=True)

    def set_order_info(self, products_list):
        self.order_info = json.dumps(products_list)

    def get_order_info(self):
        return json.loads(self.order_info)