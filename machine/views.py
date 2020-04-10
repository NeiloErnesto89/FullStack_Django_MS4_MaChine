from django.shortcuts import render
from django.http import HttpResponse
import datetime


def current_datetime(request):
    now = datetime.datetime.now()
    formatdate = now.strftime("%d-%m-%Y & the time is: %H:%M:%S")  # ("%Y-%m-%d")
    html = "<html><body><h1>Today's date is: %s.</h1></body></html>" % formatdate
    return HttpResponse(html)


def hours_ahead(request, offset):
    offset = int(offset)  # comment out to view typeerror
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    formatfuture = dt.strftime("%d-%m-%Y %H:%M:%S")
    html = "<html><body><h1>In %s hour(s), it will be %s.</h1></body></html>" % (offset,formatfuture)
    # assert False to trigger print('error')
    return HttpResponse(html)