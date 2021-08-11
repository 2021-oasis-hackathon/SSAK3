from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurant

# Create your views here.
def home(request):
    restaurants = Restaurant.objects.all()

    return render(request, 'userApp/home.html',{'restaurants' : restaurants})

def detail(request, pk):
    object = Restaurant.objects.get(pk=pk)

    context={
        'object' : object,
    }
    return render(request, 'userApp/detail.html', context)

def reservation(request, pk):
    context={'pk' : pk}
    return render(request, 'userApp/reservation.html', context)