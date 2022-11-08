from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from goods.models import Product



class Feedback(models.Model):
    product = models.ForeignKey(Product, related_name='feedback', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    date = models.DateTimeField(auto_now_add=True)
