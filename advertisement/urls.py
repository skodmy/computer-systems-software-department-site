from django.conf.urls import url

from .views import index, single, page

urlpatterns = [
    url(r'^$', index),
    url(r'^id(?P<id>\d+)/$', single),
    url(r'^page(?P<number>\d+)/$', page),
]
