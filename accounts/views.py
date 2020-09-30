from django.shortcuts import render, HttpResponse, redirect, reverse
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import Mess, Profile
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


def user_profile(request):

    if request.user.is_authenticated:
        user = User.objects.get(email=request.user.email)
    else:
        return redirect('login')
   
    return render(request, 'profile.html', {"profile": user})


# @login_required
# def update_profile(request):
#     if request.method == 'POST':
#         user_form = UserCreationForm(request.POST, instance=request.user)
#         profile_form = ProfileForm(request.POST, instance=request.user.profile)# added at the end of forms
#         if user_form.is_valid() and profile_form.is_valid():
#             user_form.save()
#             profile_form.save()
#             messages.success(request, _('Your profile was successfully updated!'))
#             return render(request, 'profile.html', {"profile": user_form})
#         else:
#             messages.error(request, 'Please correct the error below.')
#     else:
#         user_form = UserCreationForm(instance=request.user)
#         profile_form = ProfileForm(instance=request.user.profile)
#     return render(request, 'profile.html', {
#         'user_form': user_form,
#         'profile_form': profile_form
#     })

# def bio(request):
#     biof = Profile.objects.all()
#     return render(request,  'edit_profile.html', {'biof': biof})


# def delete_user(request, pk):

#     user = get_object_or_404(User, pk=pk)
#     owner = User.author
#     # return HttpResponseRedirect

#     if request.user.is_authenticated and request.user == owner:
#         posts.delete()
#         messages.success(request, 'Your post has been deleted')
#         return redirect(reverse("retrieve_posts"))

#     elif request.user.is_authenticated and request.user.is_superuser:
#         posts.delete()
#         messages.success(request, 'The admin has deleted this post')
#         return redirect(reverse("retrieve_posts"))

#     else:
#         messages.error(request, 'you are not allowed to deleted this post')
#         return redirect('post_info', posts.pk)