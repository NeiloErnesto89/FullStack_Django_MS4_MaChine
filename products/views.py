from django.shortcuts import render
from .models import Product
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# added on 28/09
def pagination(request, post_list):

    page = request.GET.get('page', 1)
    paginator = Paginator(post_list, 2)
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    except EmptyPage:
        post_list = paginator.page(paginator.num_pages)
    return post_list


# Create your views here.
def all_products(request):
    products = Product.objects.all()
    products = pagination(request, products)
    return render(request, "products.html", {"products": products})