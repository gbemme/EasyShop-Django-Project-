# Generated by Django 2.2.4 on 2019-11-14 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='product',
            fields=[
                ('product_id', models.IntegerField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=200)),
                ('produty_quantiy', models.IntegerField()),
                ('product_price', models.IntegerField()),
            ],
        ),
    ]
