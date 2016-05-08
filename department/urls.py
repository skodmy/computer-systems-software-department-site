from django.conf.urls import url
from . views import index, ajax_login, manual_logout

urlpatterns = [
    url(r'^$', index),  # if something wrong with urls then don't forget to check this
    url(r'^login/$', ajax_login),
    url(r'^logout/$', manual_logout),
]
