from django.contrib import admin
from .models import Restaurant, CartItem

# Register your models here.

admin.site.register(Restaurant)
admin.site.register(CartItem)