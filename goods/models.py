from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.urls import reverse
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(default='', null=False, blank=True, db_index=True)

    def get_url(self):
        return reverse('category-detail', args=[self.slug])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args,**kwargs)

    def __str__(self):
        return self.name

class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80)
    part_number = models.CharField(max_length=30)
    discription = models.TextField()
    amount = models.PositiveIntegerField()
    price = models.DecimalField(validators=[MinValueValidator(1)], max_digits=10, decimal_places=2)
    EURO = 'EUR'
    USD = 'USD'
    CURRENCY_CHOICES = [
        (EURO, 'Euro'),
        (USD, 'Dollars'),
    ]
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES, default='USD')
    picture = models.ImageField(upload_to = 'uploads/', verbose_name='Product Image', null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    on_moderation = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.category} - {self.name} - {self.owner}'

    def get_url(self):
        return f'{self.category.slug }/{ self.id }'


class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.PositiveIntegerField()
