# Generated by Django 4.1.1 on 2022-10-10 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_product_on_modiration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='static/uploads/', verbose_name='Product Image'),
        ),
    ]
