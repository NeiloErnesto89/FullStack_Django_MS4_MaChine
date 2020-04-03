from django.shortcuts import render
from django.http import HttpResponse
import datetime


def current_datetime(request):
    now = datetime.datetime.now()
    formatdate = now.strftime("%d-%m-%Y %H:%M:%S")  # ("%Y-%m-%d")
    html = "<html><body>It is currently %s.</body></html>" % formatdate
    return HttpResponse(html)


def hours_ahead(request, offset):
    offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    formatfuture = dt.strftime("%d-%m-%Y %H:%M:%S")
    html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, formatfuture)
    return HttpResponse(html)


