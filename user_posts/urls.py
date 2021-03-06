from django.conf.urls import url, include
# from django.urls import path
from .views import retrieve_posts, post_info, create_or_adapt_post, delete_posts, like_post  # Pagination

urlpatterns = [
    url(r'^$', retrieve_posts, name='retrieve_posts'),
    url(r'^(?P<pk>\d+)/$', post_info, name='post_info'),
    url(r'^new/$', create_or_adapt_post, name='new_post'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_adapt_post, name='edit_post'),
    #url(r'^delete/(?P<pk>\d+)/$', delete_posts, name="delete_posts"),
    url(r'^delete/(?P<pk>\d+)/$', delete_posts, name='delete_posts'),
    url(r'^like/(?P<pk>\d+)/$', like_post, name='like_post')

]