from django.conf.urls import url
from . views import carousel

urlpatterns = [
    url(r'^partners-carousel/', carousel),
]
