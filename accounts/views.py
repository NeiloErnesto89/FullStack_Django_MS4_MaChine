from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib import auth, messages


def say_hello(request):
    return HttpResponse("Hello World!")


def index(request):
    return render(request,  'index.html')


def logout(request):
    auth.logout(request)  # request contains user object
    messages.success(request, "You are now logged out!")
    return redirect(reverse('index'))  
    # pass in name of url we want to be redirect to