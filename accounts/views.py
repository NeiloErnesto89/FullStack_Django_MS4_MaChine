from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .models import Mess
from accounts.forms import UserLoginForm


def say_hello(request):
    return HttpResponse("Hello World!")


def index(request):
    messing = Mess.objects.all()
    return render(request,  'index.html', {'messes': messing})

@login_required
def logout(request):
    auth.logout(request)  # request contains user object
    messages.success(request, "You are now logged out!")
    return redirect(reverse('index'))  
    # pass in name of url we want to be redirect to


def login(request):

    if request.user.is_authenticated:
        return redirect(reverse('index'))

    if request.method == 'POST':
        login_form = UserLoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST['username'],   password=request.POST['password'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have logged in successfully")
                return redirect(reverse('index'))
            else:
                login_form.add_error(None, "Your username or password is incorrect!")
    else:
        login_form = UserLoginForm()

    return render(request, 'login.html', {'login_form': login_form})
    # value = name of the form instance just created

