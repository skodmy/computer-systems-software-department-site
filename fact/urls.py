from django.conf.urls import url

from .views import rows, facts_arguments_json

urlpatterns = [
    url(r'^rows/', rows),
    url(r'^facts-arguments-json/', facts_arguments_json),
]
