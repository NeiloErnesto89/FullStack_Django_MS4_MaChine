from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib import auth, messages
from .models import Mess
from accounts.forms import UserLoginForm


def say_hello(request):
    return HttpResponse("Hello World!")


def index(request):
    messing = Mess.objects.all()
    return render(request,  'index.html', {'messes': messing})


def logout(request):
    auth.logout(request)  # request contains user object
    messages.success(request, "You are now logged out!")
    return redirect(reverse('index'))  
    # pass in name of url we want to be redirect to


def login(request):
    login_form = UserLoginForm()
    return render(request, 'login.html', {'login_form': login_form})
    # value = name of the form instance just created