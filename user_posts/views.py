from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import User_Posts
from .forms import UserPostForm
#from django.contrib.auth.decorators import login_required
#from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# https://codeloop.org/django-pagination-complete-example/


# def Pagination(request, posts):

#     post_list = User_Posts.objects.all()
#     paginator = Paginator(post_list, 5)
#     page = request.GET.get('page', 1)
 
#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         posts = paginator.page(1)
 
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)
 
#     # return render(request, 'user_posts.html', {'page': page , 'posts': posts})
#     return posts


def retrieve_posts(request):
    posts = User_Posts.objects.filter(published_date__lte=timezone.now()
    ).order_by('-published_date')
    return render(request, "userposts.html", {'posts': posts})

def post_info(request, pk):

    post = get_object_or_404(User_Posts, pk=pk)
    post.views += 1
    post.save()
    return render(request, "postinfo.html", {'post': post})

#@login_required(login_url="accounts/login")


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

