from django.urls import path
from . import views

app_name = 'userApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('main/', views.main, name="main"),
    path('store/', views.store, name="store"),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('addCart/<int:object_pk>', views.addCart, name='addCart'),
    path('cart/', views.cart, name='cart'),
    path('pay/<int:pay>', views.pay, name='pay'),
    path('accFinish', views.accFinish, name="accFinish"),
]