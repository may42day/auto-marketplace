# Generated by Django 4.1.2 on 2022-11-22 12:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("goods", "0006_alter_currencyrate_options"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("full_name", models.CharField(max_length=40, null=True)),
                ("address", models.CharField(max_length=60, null=True)),
                ("postal_code", models.CharField(max_length=10, null=True)),
                ("phone_number", models.CharField(max_length=10, null=True)),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("PLACE", "Placing"),
                            ("OPEN", "Open"),
                            ("CANCELED", "Canceled"),
                            ("DELIVERED", "Delivered"),
                        ],
                        default="PLACE",
                        max_length=9,
                    ),
                ),
                ("comment", models.CharField(blank=True, max_length=60, null=True)),
                (
                    "currency",
                    models.CharField(
                        choices=[("EURO", "Euro"), ("USD", "Dollars")],
                        default="Euro",
                        max_length=7,
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("amount", models.PositiveIntegerField(default=1)),
                ("price", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="items",
                        to="cart.order",
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="products",
                        to="goods.product",
                    ),
                ),
            ],
        ),
    ]
