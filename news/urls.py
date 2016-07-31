from django.conf.urls import url

from .views import index, single_news, toggle_page

urlpatterns = [
    url(r'^$', index),
    url(r'^id(?P<id>\d+)/$', single_news),
    url(r'^page_number(?P<page_number>\d+)/$', toggle_page),
]
