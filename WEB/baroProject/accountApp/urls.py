from django.urls import path
from . import views

app_name = 'accountApp'

urlpatterns = [
    path('login/', views.login, name='login'),
]