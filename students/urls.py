
from django.conf.urls import url

from students import views


urlpatterns = [

    url(r'^$',views.students_rating, name='rating'),

]
