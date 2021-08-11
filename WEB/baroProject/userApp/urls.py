from django.urls import path
from . import views

app_name = 'userApp'

urlpatterns = [
    path('', views.home, name='home'),
    path('detail/<int:pk>', views.detail, name='detail'),
    path('reservation/<int:pk>', views.reservation, name="reservation"),
]