from django.urls import path
from . import views

app_name = 'accountApp'

urlpatterns = [
    path('login/<int:usertype>', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('signup/', views.signup, name='signup'),
]