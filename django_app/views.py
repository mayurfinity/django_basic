from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse,reverse_lazy
from django_app.models import StudUser
# Create your views here.

def stud(request):
    if request.method == 'POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        email=request.POST['email']
        address=request.POST['address']
        birthdate=request.POST['birthdate']
        phoneno=request.POST['phoneno']
        gender=request.POST['gender']
        file=request.POST['file']
        image=request.POST['image']

        user=StudUser.objects.create(firstname=firstname,lastname=lastname,
                                    email=email,address=address,
                                    birthdate=birthdate,phoneno=phoneno,
                                    gender=gender,file=file,image=image) #insert data
        return HttpResponseRedirect(reverse('django_app:stud'))
    else:
        return render(request,'django_app/stud.html')



def studuser(request):
    studuser=StudUser.objects.all() #to fetch all record
    date_dict={'studuser':studuser}
    return render(request,'django_app/index.html',date_dict) #to display record that page will be written is here 