from django.conf.urls import url, include
from .views import news, advertisements, news_single_article, advertisement

news_urlpatterns = [
    url(r'^page-(?P<page_number>\d+)/$', news),
    url(r'^article-(?P<article_id>\d+)/$', news_single_article),
]

advertisements_urlpatterns = [
    url(r'^page-(?P<page_number>\d+)/$', advertisements),
    url(r'^advertisement-(?P<advertisement_id>\d+)/$', advertisement),
]

urlpatterns = [
    url(r'^news/', include(news_urlpatterns)),
    url(r'^advertisements/', include(advertisements_urlpatterns)),
]
