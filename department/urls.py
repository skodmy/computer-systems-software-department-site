from django.conf.urls import url
from . views import index

urlpatterns = [
    url(r'^$', index),  # if something wrong with urls then don't forget to check this
]
