from django.conf.urls import url

from .views import cards_list, index, single

urlpatterns = [
    url(r'^$', index),
    url(r'^id(?P<id>\d+)/$', single),
    url(r'^cards-list/$', cards_list),
]
