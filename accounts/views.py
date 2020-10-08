from django.shortcuts import render, HttpResponse, redirect, reverse, get_object_or_404
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Mess, Profile
from checkout.models import Order, OrderLineItem
from accounts.forms import UserLoginForm, UserCreationForm, ProfileForm


def say_hello(request):
    return HttpResponse("Hello World!")


# def index(request):
#     messing = Mess.objects.all()
#     return render(request,  'index.html', {'messes': messing})


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


def registration(request):
    if request.user.is_authenticated:
        return redirect(reverse('index'))
    
    if request.method == "POST":
        registration_form = UserCreationForm(request.POST)  # instance of form 

        if registration_form.is_valid():
            registration_form.save()
           
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "Congrats! You have successfully registered!")
                return redirect(reverse('index'))
            else:
                messages.error(request, "We can't register your account at the moment")
    else:
        registration_form = UserCreationForm()
    #request object
    return render(request, 'registration.html', {"registration_form": registration_form})  # context dict key + (value - name of instance above)


@login_required
def user_profile(request):

    if request.user.is_authenticated:     
        user = User.objects.get(email=request.user.email)
        # order = request.session['order']
        # profile = User.objects.get(profile=request.user.profile)
        # orders = Order.objects.filter(userprofile=request.user)
    else:
        messages.warning(request, ('Please Login or Sign up'))
        return redirect('login')
   
    return render(request, 'profile.html', {"profile": user})


@login_required
def edit_profile(request):
    if request.user.is_authenticated:
        user = User.objects.get(email=request.user.email)
        
        if request.method == "POST":
            # user_form = UserCreationForm(request.FILES, instance=request.user)
            profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
            print(profile_form)
            if profile_form.is_valid():  # user_form.is_valid() and 
                # user_form.save()
                profile_form.save()
                messages.success(request, ('Your profile was successfully updated!'))
                return render(request, 'profile.html', {'profile_form': profile_form})  # 'user_form': user_form, 
            else:
                messages.error(request, 'forms not valid')
                # profile_form = ProfileForm()

        else:
            # user_form = UserCreationForm(request.FILES, instance=request.user)
            profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        return render(request, 'edit_profile.html', {
            # 'user_form': user_form,
            'profile_form': profile_form
            })
    else:
        return redirect('login')

@login_required
def delete_user(request, pk):

    user = get_object_or_404(User, pk=pk)
    # return HttpResponseRedirect

    if request.user.is_authenticated and request.user == user:
        user.delete()
        messages.success(request, 'This User has been deleted')
        return redirect(reverse("login"))

    elif request.user.is_authenticated and request.user.is_superuser:
        user.delete()
        messages.success(request, 'The admin has deleted this post')
        return redirect(reverse("index"))

    else:
        messages.error(request, 'you are not allowed to deleted this post')
        return redirect('profile', user.pk)

# added 01/10
# @login_required
# def update_profile(request):
#     if request.user.is_authenticated:
#         # user = User.objects.get(email=request.user.email)
#         if request.method == "POST":
#             registration_form = UserCreationForm(instance=request.user)
#             profile_form = ProfileForm(request.POST, instance=request.user.profile)
#             if profile_form.is_valid() and registration_form.is_valid():
#                 registration_form.save()
#                 profile_form.save()
#                 messages.success(request, _('Your profile was successfully updated!'))
#                 return render(request, 'edit_profile.html', {"user form": registration_form })
#             else:
#                 messages.error(request, 'forms not valid')
#         else:
#             registration_form = UserCreationForm(instance=request.user)
#             profile_form = ProfileForm(instance=request.user.profile)
#         return render(request, 'edit_profile.html', {
#             "user form": registration_form,
#             'profile_form': profile_form
#         })
#     else:
#         messages.error(request, 'forms not valid')
#         return redirect(reverse('login'))




