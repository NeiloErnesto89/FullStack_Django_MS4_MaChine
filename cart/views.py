from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
# from accounts.forms import UserLoginForm

# Create your views here.


@login_required
def view_cart(request):
    """A View that renders the cart contents page"""
    if request.user.is_authenticated:
        return render(request, "cart.html")  # we don't have to pass in a dictionary of cart_contents because that context is available everywhere.
    else:
        messages.error(request, "You must log in or sign up")
        return redirect(reverse('index'))


        # value = name of the form instance just created


@login_required
def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    quantity = int(request.POST.get('quantity'))

    # if quantity.is_digit() == False:

    #     messages.error(request, 'You have not added any quantity')
    #     return redirect(reverse('index'))

    # else:

    cart = request.session.get('cart', {})
    if id in cart:
        cart[id] = int(cart[id]) + quantity
    else:
        cart[id] = cart.get(id, quantity)
    # cart[id] = cart.get(id, quantity)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))


@login_required
def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity
    else:
        cart.pop(id)
    
    request.session['cart'] = cart
    return redirect(reverse('view_cart'))