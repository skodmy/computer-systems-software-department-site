from django.conf.urls import url

from .views import index, single_news

urlpatterns = [
    url(r'^$', index),
    # url(r'^index/$', index),
    url(r'^id(?P<id>\d+)/$', single_news),
]
