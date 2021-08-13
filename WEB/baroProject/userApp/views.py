from django.shortcuts import render
from django.http import HttpResponse
from .models import Restaurant

# Create your views here.
def home(request):
    return render(request, 'userApp/home.html')

def main(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'userApp/main.html',{'restaurants' : restaurants} )

def detail(request, pk):
    object = Restaurant.objects.get(pk=pk)

    context={
        'object' : object,
    }
    return render(request, 'userApp/detail.html', context)

def reservation(request, pk):
    context={'pk' : pk}
    return HttpResponse('즐겨찾기 기능 만들기')