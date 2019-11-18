from django.db import models

# Create your models here.

class Product(models.Model):
    product_id =models.IntegerField(primary_key=True)
    product_name=models.CharField(max_length=200)
    produty_quantiy = models.IntegerField()
    product_price = models.IntegerField()
    product_img = models.ImageField(upload_to = 'media',default='')

    def __str__(self):
        return(self.product_name)
        

from .models import Product
class Payment(models.Model):
    # product_id = models.ForeignKey(product.product_id,on_delete=models.CASCADE)
    card_no = models.IntegerField()
    card_type = models.CharField(max_length=30)
    address = models.CharField(max_length=100)


    