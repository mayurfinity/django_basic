from django.shortcuts import render
from django.contrib.auth import login, logout,authenticate
from django.contrib.auth.hashers import make_password
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from basic_app.models import CustUser
# Create your views here.

def index(request):
    return render(request,'basic_app/index.html')

def register(request):
    if request.method == 'POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        verify_password=request.POST['Verify_password']

        if password!=verify_password:
            error_msg='password not match !'
            data={'error_msg':error_msg}
            return render(request,'basic_app/register.html',data)
        if CustUser.objects.filter(username=username).exists():
            error_msg='username already exist !'
            data={'error_msg':error_msg}
            return render(request,'basic_app/register.html',data)
        else :
            user=CustUser.objects.create(username=username,password=make_password(password),email=email) #insert data
            login(request,user)
            return HttpResponseRedirect(reverse('basic_app:index'))
    else:
        return render(request,'basic_app/register.html')

def userlogin(request):
    if request.method == 'POST':
        username=request.POST['Username']
        password=request.POST['password']
        user=authenticate(username=username ,password=password)

        if user is not None :
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('basic_app:index'))
            else :
                error_msg='username and password wrong  !'
                data={'error_msg':error_msg}
                return render(request,'basic_app/login.html',data)
        else:
            error_msg='username and password wrong  !'
            data={'error_msg':error_msg}
            return render(request,'basic_app/login.html',data)
    else:
        return render(request,'basic_app/login.html')

def index1(request):
    custuser=CustUser.objects.all() #to fetch all record
    date_dict={'custuser':custuser}
    return render(request,'basic_app/base1.html',date_dict)

