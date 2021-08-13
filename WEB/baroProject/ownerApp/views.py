from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Store
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def main(request):
    return render(request, 'ownerApp/main.html')

def register(request):
    return render(request, 'ownerApp/register.html')

@login_required
def register2(request):
    context={}

    if request.method == "POST":
        
        store = Store.objects.create(
            user = User.objects.get(username = request.user.get_username()) ,
            store_name = request.POST['store_name'],
            store_url = request.POST['store_url'],
            store_intro = request.POST['store_intro'],
            store_tel = request.POST['store_tel'],
            category = request.POST['category'],
            store_address = request.POST['store_address'],
            store_account = request.POST['store_account'] ,
        )

        store_pk = Store.pk
        context['store_pk'] = store_pk
        return redirect( 'ownerApp:register3', store_pk)
    else: #GET Method
        return render(request, 'ownerApp/register2.html')

def register3(request, store_pk):
    context={}
    try:
        store = Store.objects.get(pk=store_pk)
    except Store.DoesNotExist:
        print("상점 불러오기 에러")
        return redirect('userApp:home')
    context['store'] = store
    return render( request, 'ownerApp/register3.html', context)

def manage(request):
    return HttpResponse('관리페이지')

def help(request):
    return HttpResponse('생산지원페이지입니다')