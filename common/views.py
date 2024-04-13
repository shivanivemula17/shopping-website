from django.shortcuts import render,redirect
from django.http import HttpResponse
from django. contrib. auth.models import User,auth
from django.contrib.auth import authenticate,login,logout
from django. contrib import messages
# Create your views here.
def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')
def module_admin(request):
    return render(request,'module_admin.html')
def module_manager(request):
    return render(request,'module_manager.html')
def module_user(request):
    return render(request,'module_user.html')
def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']  
        #message = username+password 
        user=auth.authenticate(request, username=username,password=password)
        if user is not None:
            if user.last_name == 'manager':
                return redirect('manager')
            else:
                return redirect('user')
        else:
            return render(request,'login.html',{'result':"failed"})
    else:
        return render(request,'login.html')
def contact(request):
    if request.method == 'POST':
        FullName=request.POST['Name']
        Email=request.POST['email']
        TypeYourMessage=request.POST['textarea']
        message = FullName+Email+TypeYourMessage
        return render(request,'contact.html',{'result':message})
    else:
        return render(request,'contact.html',{'result':"inside else"})
def signup(request):
    if request.method == 'POST':
        Firstname=request.POST['fullname']
        Lastname=request.POST['lastname']
        email=request.POST['emailaddress']
        #phonenumber=request.POST['number']
        category=request.POST['category']
        username=request.POST['pickausername']
        password=request.POST['setapassword']
        if User.objects.filter(username=username).exists():
             return redirect('/')
        else:
            user=User.objects.create_user(first_name=Firstname,last_name=Lastname,email=email,username=username,password=password)    
            user.save();
            messages.info(request,'user created')
            return render(request,'signup.html',{'result':"inside else"})
    else:
        return render(request,'signup.html',{'result':"inside else"})
    