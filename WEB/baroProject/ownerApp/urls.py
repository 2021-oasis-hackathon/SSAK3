from django.urls import path
from . import views

app_name = 'ownerApp'

urlpatterns = [
    path('main/', views.main, name='main'),
]