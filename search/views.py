from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from products.models import Product


# Create your views here.
def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])

    if products.exists():
        return render(request, "products.html", {"products": products})
 
    else:
        messages.success(request, "No Such Product Exists. \n Try searching for 'Raspberry Pi'")
        return redirect(reverse("index"))
