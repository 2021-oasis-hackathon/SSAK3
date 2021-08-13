from django.urls import path
from . import views

app_name = 'ownerApp'

urlpatterns = [
    path('main/', views.main, name='main'),
    path('manage/', views.manage, name='manage'),
    path('register/', views.register, name='register'),
    path('register2/', views.register2, name='register2'),
    path('register3/<int:store_pk>', views.register3, name='register3'),
    path('help/', views.help, name='help'),
]