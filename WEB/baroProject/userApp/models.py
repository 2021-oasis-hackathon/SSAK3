from django.db import models

# Create your models here.

class Restaurant(models.Model):
    name = models.CharField(max_length=30)
    style = models.CharField(max_length=30)
    review = models.IntegerField()
    star = models.FloatField()
    
    def __str__(self):
        return f'{self.pk} : {self.name} | {self.style}'