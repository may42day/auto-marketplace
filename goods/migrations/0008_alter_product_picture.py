# Generated by Django 4.1.1 on 2022-10-10 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0007_alter_product_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='uploads/', verbose_name='Product Image'),
        ),
    ]
