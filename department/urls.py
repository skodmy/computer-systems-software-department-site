from django.conf.urls import url
from . views import index, ajax_login, manual_logout, slides, contacts, applicant_in_general, under_development, \
    about_specialization

urlpatterns = [
    url(r'^$', index),  # if something wrong with urls then don't forget to check this
    url(r'^login/$', ajax_login),
    url(r'^logout/$', manual_logout),
    url(r'^slides/$', slides),
    url(r'^contacts/$', contacts),
    url(r'^applicant-in-general/$', applicant_in_general),
    url(r'^about-specialization/$', about_specialization),
    url(r'^under-development/$', under_development),
]
