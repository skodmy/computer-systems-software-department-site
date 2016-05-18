from django.conf.urls import url

from .views import cards_list, news_details

urlpatterns = [
    url(r'^cards-list/$', cards_list),
    url(r'^news-details/$', news_details)
]
