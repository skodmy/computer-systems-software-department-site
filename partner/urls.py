from django.conf.urls import url
from . views import carousel_items_list

urlpatterns = [
    url(r'^carousel-items-list/', carousel_items_list),
]
