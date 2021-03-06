from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .models import info

# Create your views here.

def signup(request, usertype):
    context={}
    # POST Method
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        password_check = request.POST['password_check']
        usertype = request.POST['usertype']

        # 제대로 입력되었을 경우
        if (username and password and password_check == password):
            new_user = User.objects.create_user(
                username = username,
                password = password,
            )
            new_info=info.objects.create(
                user=User.objects.get(username = username),
                usertype = request.POST['usertype'],
                )

            return redirect('accountApp:signupSuccess')
        else:
            context['error'] = "아이디와 비밀번호를 다시 확인해주세요."

    # GET Method
    context['usertype'] = usertype
    return render(request, 'accountApp/signup.html', context)


def login(request, usertype):
    context={}

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        usertype = int(request.POST.get('usertype', ''))
        if username and password:
            user = auth.authenticate(
                request,
                username = username,
                password = password
            )
            if user is not None:
                # 사용자가 있으면 로그인후 home으로
                auth.login(request, user)
                ut = int(info.objects.get(user=user).usertype)
                # if (ut =="판매자" or ut==1): ut = 1
                # elif ut =="구매자" or ut ==2 : ut=2
                if ut != usertype:
                    auth.logout(request)
                    context['error'] = "로그인 유형을 다시 선택하세요."
                    print("유저홈")
                    return redirect('userApp:home')
                elif usertype == 1: #생산자
                    print("생산자 manage")
                    return redirect('ownerApp:manage')
                elif usertype == 2: #소비자
                    print("유저홈")
                    return redirect('userApp:main')
            else:
                print("에러1")
                context['error'] = '아이디와 비밀번호를 다시 확인해주세요.'
        else:
            #아이디나 비밀번호가 제대로 입력되지 않았을때
            print("에러2")
            context['error'] = '아이디와 비밀번호를 모두 입력해주세요.'

    # Get Method
    print("설마여기")
    print(usertype)
    context['usertype'] = usertype
    return render(request, 'accountApp/login2.html', context)

def logout(request):
    if request.method == "POST":
        auth.logout(request)
    # 로그아웃하면 이전 페이지로
    #return redirect(request.POST['path'])
    # 로그아웃하면 홈으로
    return redirect("userApp:home")
   

def signupAgree(request):
    return render(request, 'accountApp/signupAgree.html')

def signupSuccess(request):
    return render(request, 'accountApp/signupSuccess.html')