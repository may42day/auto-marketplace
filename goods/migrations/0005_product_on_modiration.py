# Generated by Django 4.1.1 on 2022-10-10 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0004_alter_product_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='on_modiration',
            field=models.BooleanField(default=True),
        ),
    ]
