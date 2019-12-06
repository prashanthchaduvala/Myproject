import random

from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import LoginForm
from .models import loginpage,Otp
from django.core.mail import send_mail
from login import settings as se
# Create your views here.
def signup(request):
    fm=LoginForm()
    return render(request,'login.html',{'form':fm})


def login(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        form.save()
        messages.success(request,"successfully registered..")
        return redirect('/')
    else:
        messages.error(request,"not saved")
        return redirect('/')


def signin(request):
    return render(request,"signin.html",{"form":LoginForm()})


def checklogin(request):
    email=request.POST.get('email')
    pas=request.POST.get('password')
    try:
      if loginpage.objects.get(email=email,password=pas):
        return render(request,'wellcome.html',{'message':email})
      else:
        messages.error(request,'invalid username or password')
        return redirect('log')
    except loginpage.DoesNotExist:
        messages.error(request, 'invalid username or password')
        return redirect('log')


def reset(request):
    return render(request,"reset.html")


def checkemail(request):
    email=request.POST.get('email')
    if loginpage.objects.get(email=email):
        otp = str(random.randint(1111,9999))
        Otp(otp=otp).save()
        send_mail('OTP',"Use this otp to reset new password",se.EMAIL_HOST_USER,["email"])
        return render(request,'otp.html')
    else:
        messages.error(request,'invalid email')
        return redirect('reset')


def validotp(request):
    otp=request.POST.get('otp')
    Otp.objects.get(otp=otp).delete()
    return render(request,'newpass.html')


def topic(request):
    return render(request,'topic.html')


def book(request):
    return render(request,'book.html',{'message':'Thanks for viiting'})


def details(request):
    return render(request,'bookdetails.html')