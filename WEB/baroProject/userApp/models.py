from django.db import models
from django.contrib.auth.models import User
from ownerApp.models import Product
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    style = models.CharField(max_length=30)
    review = models.IntegerField()
    star = models.FloatField()
    
    def __str__(self):
        return f'{self.pk} : {self.name} | {self.style}'

class CartItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    od_amount = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(100)])
    od_date = models.DateField()
    # DELIERY=[("icepack","아이스팩"), ("premium", "신선배송가방")]
    od_deliopt = models.CharField(max_length=30)
    od_requests=models.TextField(null=True)

    #https://dev-mht.tistory.com/147
    def sub_total(self):
        return int(self.product.price * self.od_amount)

    def __str__(self):
        return f'{self.products} - {self.od_amount} : {self.sub_total}'
