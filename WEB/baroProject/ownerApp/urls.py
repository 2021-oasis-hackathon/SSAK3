from django.urls import path
from . import views

app_name = 'ownerApp'

urlpatterns = [
    path('main/', views.main, name='main'),
    path('manage/', views.manage, name='manage'),
    path('register/', views.register, name='register'),
    path('help/', views.help, name='help'),
]