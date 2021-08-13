from django.db import models
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