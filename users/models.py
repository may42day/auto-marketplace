from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    CUSTOMER = 'Customer'
    SELLER = 'Seller'
    USER_TYPES = [
        (CUSTOMER, 'Customer'),
        (SELLER, 'Seller')
    ]
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_type = models.CharField(max_length=8, choices=USER_TYPES, default='Customer')

    def __str__(self):
        if self.user_type == self.CUSTOMER:
            return f'Customer {self.user}'
        else:
            return f'Seller {self.user}'

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

