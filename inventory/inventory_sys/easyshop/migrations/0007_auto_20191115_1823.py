# Generated by Django 2.2.4 on 2019-11-15 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('easyshop', '0006_product_product_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_img',
            field=models.ImageField(default='', height_field='400', upload_to='media', width_field='800'),
        ),
    ]