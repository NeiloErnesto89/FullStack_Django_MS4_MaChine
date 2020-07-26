import re
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from .models import User_Posts
from .forms import UserPostForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# from django.views.generic import ListView



# https://codeloop.org/django-pagination-complete-example/

# class UserPostListView(ListView):
#     model = User_Posts
#     paginate_by = 3
#     template_name = 'user_posts/userposts.html'
#     context_object_name = 'user_posts'
#     ordering = ['-published_date']


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

@login_required
def retrieve_posts(request):
    
    posts = User_Posts.objects.filter(published_date__lte=timezone.now()
    ).order_by('-published_date')

    posts = pagination(request, posts)

    return render(request, "userposts.html", {'posts': posts})


@login_required
def post_info(request, pk):

    post = get_object_or_404(User_Posts, pk=pk)
    post.views += 1
    post.save()
    return render(request, "postinfo.html", {'post': post})

#@login_required(login_url="accounts/login")

@login_required
def create_or_adapt_post(request, pk=None):

    post = get_object_or_404(User_Posts, pk=pk) if pk else None
    if request.method == "POST":
        form = UserPostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()  
            #post = form.save()
            return redirect(post_info, post.pk)
    else:
        form = UserPostForm(instance=post)
    return render(request, 'userpostform.html', {'form': form})


@login_required
def delete_posts(request, pk):

    posts = get_object_or_404(User_Posts, pk=pk)
    owner = posts.author
    # return HttpResponseRedirect

    if request.user.is_authenticated and request.user == owner:
        posts.delete()
        messages.success(request, 'Your post has been deleted')
        return redirect(reverse("retrieve_posts"))

    elif request.user.is_authenticated and request.user.is_superuser:
        posts.delete()
        messages.success(request, 'The admin has deleted this post')
        return redirect(reverse("retrieve_posts"))

    else:
        messages.error(request, 'you are not allowed to deleted this post')
        return redirect('post_info', posts.pk)


