from django.conf.urls import url

from .views import divs_list

urlpatterns = [
    url(r'^divs-list/', divs_list)
]