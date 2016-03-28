from django.conf.urls import url

from .views import cards_list

urlpatterns = [
    url(r'^cards-list', cards_list)
]