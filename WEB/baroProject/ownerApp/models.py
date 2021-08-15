from django.db import models
import os
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.



class Store(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    store_name = models.CharField(max_length=30)
    store_url = models.CharField(max_length=30)
    store_intro = models.TextField()
    store_tel = models.CharField(max_length=30)
    CATEGORYLIST=[('veg', "채소/야채"), ('fruits', "과일"), ('grains', "곡류")]
    category = models.CharField(
        choices=CATEGORYLIST, max_length=30, null=True, blank=True)
    store_address=models.CharField(max_length=100)
    BANKLIST=[('NH', "농협"), ('KB', "국민"), ('SH', "신한"), ('etc', "기타")]
    bank = models.CharField(
        choices=BANKLIST, max_length=30, null=True, blank=True)
    account_name = models.CharField(max_length=30, null=True, blank=True)
    store_account=models.CharField(max_length=50)
    

    def __str__(self):
        return f'{self.pk} : {self.store_name} : {self.user}'


class Product(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name =  models.CharField(max_length=30)
    price = models.FloatField()
    intro = models.TextField()
    Thumbnail = models.ImageField(upload_to='thumimg', null=True)
    introImage = models.ImageField(upload_to='productimg', null=True)
    salesRate = models.IntegerField(default=0, null=True)
    OPTLIST=[('opt1', 'opt1'),('opt2', 'opt2'),('opt3', 'opt3'),('opt4', 'opt4')]
    category = models.CharField(
        choices=OPTLIST, max_length=30, null=True)
    expect = models.CharField(max_length=50, null=True)
    amount = models.CharField(max_length=30, null=True)
    expectD1 = models.DateField(null=True)
    expectD2 = models.DateField(null=True)
    deliveryD1 = models.DateField(null=True)
    deliveryD2 = models.DateField(null=True)
    DELIERY=[("icepack","아이스팩"), ("premium", "신선배송가방")]
    deliveryOption =  models.CharField(
        choices=DELIERY, max_length=30, null=True)
    region = models.CharField(max_length=50, null=True)

    def delete(self, *args, **kwargs):
        super(Product, self).delete(*args, **kwargs)
        if self.introImage : 
            os.remove(os.path.join(settings.MEDIA_ROOT, self.introImage.path))

    def __str__(self):
        return f'{self.pk} : {self.store} : {self.name}'

# 미디어 파일 참조링크  https://wayhome25.github.io/django/2017/05/10/media-file/
