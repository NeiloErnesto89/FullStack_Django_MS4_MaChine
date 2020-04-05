from django.shortcuts import render, HttpResponse


def say_hello(request):
    return HttpResponse("Hello World!")


def index(request):
    return render(request,  'index.html')
