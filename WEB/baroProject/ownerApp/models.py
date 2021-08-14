from django.db import models
import os
from django.conf import settings
from django.contrib.auth.models import User
# Create your models here.



class Store(models.Model):
    user = user=models.ForeignKey(User,on_delete=models.CASCADE)
    store_name = models.CharField(max_length=30)
    store_url = models.CharField(max_length=30)
    store_intro = models.TextField()
    store_tel = models.CharField(max_length=30)
    CATEGORYLIST=[('veg', "채소/야채"), ('fruits', "과일"), ('grains', "곡류")]
    category = models.CharField(
        choices=CATEGORYLIST, max_length=30, null=True, blank=True)
    store_address=models.CharField(max_length=100)
    store_account=models.CharField(max_length=50)
    

    def __str__(self):
        return f'{self.pk} : {self.store_name} - {self.user}'


class Product(model.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    name =  models.CharField(max_length=30)
    price = models.FloatField()
    intro = models.TextField()
    Thumbnail = models.ImageField(upload_to='thumimg', null=True)
    introImage = models.ImageField(upload_to='productimg', null=True)

    def delete(sef, *args, **kwargs):
        super(Product, self).delete(*args, **kwargs)
        if self.introImage : 
            os.remove(os.path.join(settings.MEDIA_ROOT, self.introImage.path))

# 미디어 파일 참조링크  https://wayhome25.github.io/django/2017/05/10/media-file/
