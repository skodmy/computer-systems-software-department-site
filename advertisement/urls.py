from django.conf.urls import url

from .views import actual_cards_list

urlpatterns = [
    url(r'^actual-cards-list/', actual_cards_list)
]