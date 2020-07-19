from django.conf.urls import url, include
# from django.urls import path
from .views import retrieve_posts, post_info, create_or_adapt_post  # Pagination

urlpatterns = [
    url(r'^$', retrieve_posts, name='retrieve_posts'),
    url(r'^(?P<pk>\d+)/$', post_info, name='post_info'),
    url(r'^new/$', create_or_adapt_post, name='new_post'),
    url(r'^(?P<pk>\d+)/edit/$', create_or_adapt_post, name='edit_post')
]