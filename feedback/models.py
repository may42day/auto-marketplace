from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg
from goods.models import Product


RAITING_CHOICES = [(f"{i}", f"{i}") for i in range(1, 6)]


class Feedback(models.Model):
    product = models.ForeignKey(
        Product, related_name="feedback", on_delete=models.CASCADE
    )
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    text = models.TextField()
    rating = models.CharField(max_length=1, choices=RAITING_CHOICES, default="5")
    date = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        super(Feedback, self).save(*args, **kwargs)
        self.calculate_average_rating(save=True)

    def calculate_average_rating(self, save=False, delete=False, exclude_pk=None):
        product = self.product
        avg_rating = (
            Feedback.objects.filter(product=product)
            .exclude(pk=exclude_pk)
            .aggregate(Avg("rating"))["rating__avg"]
        )
        if avg_rating:
            product.average_rating = round(avg_rating, 1)
        else:
            product.average_rating = 0
        if save:
            product.feedback_counter += 1
        elif delete:
            product.feedback_counter -= 1
        product.save()
