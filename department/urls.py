from django.conf.urls import url
from . views import index, ajax_login, manual_logout, contacts, applicant_in_general, under_development, \
    about_specialization, academic_subjects, useful_links, schedule

urlpatterns = [
    url(r'^$', index),  # if something wrong with urls then don't forget to check this
    url(r'^login/$', ajax_login),
    url(r'^logout/$', manual_logout),
    url(r'^contacts/$', contacts),
    url(r'^applicant-in-general/$', applicant_in_general),
    url(r'^about-specialization/$', about_specialization),
    url(r'^academic-subjects/$', academic_subjects),
    url(r'^useful-links/$', useful_links),
    url(r'^schedule/$', schedule),
    url(r'^under-development/$', under_development),
]
