from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def main(request):
    return render(request, 'ownerApp/main.html')

def register(request):
    return HttpResponse('등록페이지')

def manage(request):
    return HttpResponse('관리페이지')

def help(request):
    return HttpResponse('생산지원페이지입니다')