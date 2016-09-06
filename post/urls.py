from django.conf.urls import url, include
from .views import news, attentors, news_single_article, attentor

news_urlpatterns = [
    url(r'^page-(?P<page_number>\d+)/$', news),
    url(r'^article-(?P<article_id>\d+)/$', news_single_article),
]

attentors_urlpatterns = [
    url(r'^page-(?P<page_number>\d+)/$', attentors),
    url(r'^attentor-(?P<attentor_id>\d+)/$', attentor),
]

urlpatterns = [
    url(r'^news/', include(news_urlpatterns)),
    url(r'^attentors/', include(attentors_urlpatterns)),
]
