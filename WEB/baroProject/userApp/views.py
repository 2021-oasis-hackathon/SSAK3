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
    products = Product.objects.all()[:3]
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
            # od_requests = request.POST['od_requests'],
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
    if cart_items.count() == 0:
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

def pay(request):
    context={}
    # context['pay'] = pay
    return render(request, 'userApp/pay.html', context)

def store(request):
    context={}

    if request.method == "POST":
        sText = request.POST['searchText']
        context['sText']=sText
        #여자 #10대 #피곤
        gender, age, health = sText.split(' ')
        gender = gender.replace('#', '')
        age = age.replace('#', '')
        health = health.replace('#', '')

        FITERLIST=[(1, '-age1_M_B'),(2, '-age1_M_W'),(3, '-age1_M_G'),
                    (4, '-age1_W_B'),(5, '-age1_W_W'),(6, '-age1_W_G'),
                    (7, '-age2_M_B'),(8, '-age2_M_W'),(9, '-age2_M_G'),
                    (10, '-age2_W_B'),(11, '-age2_W_W'),(12, '-age2_W_G'),
                    (13, '-age3_M_B'),(14, '-age3_M_W'),(15, '-age3_M_G'),
                    (16, '-age3_W_B'),(17, '-age3_W_W'),(18, '-age3_W_G'),
                    (19, '-age4_M_B'),(20, '-age4_M_W'),(21, '-age4_M_G'),
                    (22, '-age4_W_B'),(23, '-age4_W_W'),(24, '-age4_W_G'),]
        

        #나이 
        if age=="10대":
            if gender=="여자":
                if health=="good":
                    fkey=FITERLIST[6-1][1]
                elif health=="worry":
                    fkey=FITERLIST[5-1][1]
                elif health=="bad":
                    fkey=FITERLIST[4-1][1]
            elif gender=="남자":
                if health=="good":
                    fkey=FITERLIST[3-1][1]
                elif health=="worry":
                    fkey=FITERLIST[2-1][1]
                elif health=="bad":
                    fkey=FITERLIST[1-1][1]
        elif age=="20대" or age=="30대":
            if gender=="여자":
                if health=="good":
                    fkey=FITERLIST[12-1][1]
                elif health=="worry":
                    fkey=FITERLIST[11-1][1]
                elif health=="bad":
                    fkey=FITERLIST[10-1][1]
            elif gender=="남자":
                if health=="good":
                    fkey=FITERLIST[9-1][1]
                elif health=="worry":
                    fkey=FITERLIST[8-1][1]
                elif health=="bad":
                    fkey=FITERLIST[7-1][1]
        elif age=="40대" or age=="50대":
            if gender=="여자":
                if health=="good":
                    fkey=FITERLIST[18-1][1]
                elif health=="worry":
                    fkey=FITERLIST[17-1][1]
                elif health=="bad":
                    fkey=FITERLIST[16-1][1]
            elif gender=="남자":
                if health=="good":
                    fkey=FITERLIST[15-1][1]
                elif health=="worry":
                    fkey=FITERLIST[14-1][1]
                elif health=="bad":
                    fkey=FITERLIST[13-1][1]
        elif age == "60대":
            if gender=="여자":
                if health=="good":
                    fkey=FITERLIST[24-1][1]
                elif health=="worry":
                    fkey=FITERLIST[23-1][1]
                elif health=="bad":
                    fkey=FITERLIST[22-1][1]
            elif gender=="남자":
                if health=="good":
                    fkey=FITERLIST[21-1][1]
                elif health=="worry":
                    fkey=FITERLIST[20-1][1]
                elif health=="bad":
                    fkey=FITERLIST[19-1][1]
        else :
            #전체판매량
            fkey = '-salesRate'

        print(fkey)
        products = Product.objects.all().order_by(fkey)[:9]
        context['products'] = products
        print(products)
        print("POST")
        return render(request, 'userApp/store.html', context)
    else :
        products = Product.objects.all()[:9]
        context['products'] = products
        return render(request, 'userApp/store.html', context)

def accFinish(request):
    return render(request, 'userApp/accFinish.html')