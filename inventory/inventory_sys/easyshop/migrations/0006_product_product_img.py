# Generated by Django 2.2.4 on 2019-11-15 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easyshop', '0005_remove_product_product_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_img',
            field=models.ImageField(default='', upload_to='media'),
        ),
    ]