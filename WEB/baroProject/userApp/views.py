from django.shortcuts import render, redirect
from django.http import HttpResponse
from ownerApp.models import Product
from .models import CartItem
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

def home(request):
    return render(request, 'userApp/home.html')

def main(request):
    context={}
    products = Product.objects.all()
    context['products'] = products
    return render(request, 'userApp/main.html',context)

def detail(request, pk):
    object = Product.objects.get(pk=pk)

    context={
        'object' : object,
    }
    return render(request, 'userApp/detail.html', context)

@login_required
def addCart(request, object_pk):
    if request.method == "POST":
        print("POST로 들어왔니")
        item = CartItem.objects.create(
            user = User.objects.get(username = request.user.get_username()) ,
            product = Product.objects.get(pk = object_pk),
            od_amount = request.POST['od_amount'],
            od_date = request.POST['od_date'],
            od_deliopt = request.POST['od_deliopt'],
            od_requests = request.POST['od_requests'],
        )
        print("아이템 생성 완료")
        return redirect('userApp:cart')
        return redirect('cart')
    else:
        print("GET요청")
        return HttpResponse("addCart GET 오류")

def cart(request):
    context={}
    total = 0
    shippingFee = 0

    cart_items = CartItem.objects.filter(user__id = request.user.pk)
    if cart_items == None:
        context['error'] = '담긴 상품이 없습니다.'
    else:
        for item in cart_items:
            total += item.sub_total()

    pay = total + shippingFee

    context['total'] = total
    context['shippingFee'] = shippingFee
    context['pay'] = pay
    context['cart_items'] = cart_items
    return render(request, 'userApp/Cart.html', context)

def pay(request, pay):
    context={}
    context['pay'] = pay
    return render(request, 'userApp/pay.html', context)

def store(request):
    context={}
    return render(request, 'userApp/store.html', context)