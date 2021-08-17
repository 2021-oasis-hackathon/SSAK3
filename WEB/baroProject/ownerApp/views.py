from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Store, Product
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required

# Create your views here.

def main(request):
    return render(request, 'ownerApp/main.html')

@login_required
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
            bank = request.POST['bank'],
            account_name = request.POST['account_name'],
            store_account = request.POST['store_account'] ,
        )
        print("상점이 생성되었음.")

        store_pk = store.pk
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
    context={}
    store = Store.objects.get(user=User.objects.get(username = request.user.get_username()))
    print(store)
    if store == None:
        return redirect("ownerApp/main")
    
    products =  Product.objects.all()[:5]
    context['products'] = products
    context['store'] = store

    return render(request, 'ownerApp/manage.html', context)

def productManage(request, storepk):
    context={}
    if request.method == "POST":
        prod = Product.objects.create(
            store = Store.objects.get(pk = storepk),
            name = request.POST['name'],
            price = request.POST['price'],
            intro = request.POST['intro_text'],
            Thumbnail = request.FILES['Thumbnail'],
            # introImage = request.POST[''],
            # salesRate = request.POST[''],
            category = request.POST['category'],
            expect = request.POST['expect'],#예상수확량
            amount = request.POST['amount'],#기준량
            expectD1 = request.POST['expectD1'],
            expectD2 = request.POST['expectD2'],
            deliveryD1 = request.POST['deliveryD1'],
            deliveryD2 = request.POST['deliveryD2'],
            deliveryOption =request.POST['deliveryOption'],
            region = request.POST['region'],
        )
        return redirect("ownerApp:manage")
    else:
        context['storepk'] = storepk
        return render(request, 'ownerApp/productManage.html', context)

def help(request):
    return HttpResponse('생산지원페이지입니다')