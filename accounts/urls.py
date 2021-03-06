from django.conf.urls import url, include
from accounts.views import logout, login, registration, user_profile, edit_profile, delete_user
#  from accounts.views import delete_account, 
from accounts import url_reset

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', registration, name="registration"),
    url(r'^profile/', user_profile, name="profile"),
    url(r'^edit-profile/', edit_profile, name="edit_profile"),
    url(r'^delete-account/(?P<pk>\d+)/$', delete_user, name="delete_user"),
    url(r'^password-reset/', include(url_reset))
]