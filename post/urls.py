from django.conf.urls import url
from .views import news, advertisements

urlpatterns = [
    url(r'^news/page-(?P<page_number>\d+)/$', news),
    url(r'^advertisements/page-(?P<page_number>\d+)/$', advertisements),
]
