from django.conf.urls import url

from .views import records, news_details

urlpatterns = [
    url(r'^records/$', records),
    url(r'^news-details/$', news_details),
]
