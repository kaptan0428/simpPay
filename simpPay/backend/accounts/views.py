from genericpath import exists
import imp
from operator import is_not

from django.shortcuts import render,redirect
from django.http import HttpResponse, request
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
# Create your views here.

def handleSignup(request):
    if request.method == 'POST':
        Fname = request.POST['fname']
        Lname = request.POST['lname']
        email = request.POST['email']
        username = request.POST['username']
        pass1 = request.POST['pass-1']
        pass2 = request.POST['pass-2']
        

        if pass1==pass2:
            if User.objects.filter(email=email).exists():
                messages.error(request,'this email is already registered')

            elif User.objects.filter(username=username).exists():
                print('email already taken')
                messages.error(request,'this username is already registered')
               
            else:
                myuser = User.objects.create_user(username=username,email=email, password=pass1,first_name=Fname,last_name=Lname)
                myuser.save()
                try:
                    user = authenticate(username=User.objects.get(email=username),password=pass1)
                except:
                    user = authenticate(username=username,password=pass1)
                if user is not None:
                    login(request,user)
                    return render(request, 'pay.html')
                else:
                    messages.error(request, 'email or password is not matching please create account first')
        else:
            messages.error(request,'both password should be same')
        
        return redirect('/')
    else:
        return render(request, 'home.html')

def loogin(request):
    if request.method == 'POST':
        # get post parameter from the user
        loginemail = request.POST['email']
        loginpassword = request.POST['pass-1']

        user = authenticate(username=User.objects.filter(email=loginemail).first(),password=loginpassword)
        if user is not None:
            login(request,user)
            messages.success(request,'Successfully logged in')
            return redirect('pay')
        else:
            messages.error(request,'Invalid username or password,Please try again')
            return redirect('/')
    else:
        return render(request, 'login.html')

        

# def loogin(request):


#     return render(request, 'login.html')

def pay(request):
    return render(request, 'pay.html')

def handle_logout(request):
        logout(request)
        messages.success(request,'Logout Successfully')
        return redirect('/')