"""pzks_departments_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

# this is only for development use
from django.conf import settings
from django.conf.urls.static import static
# -----

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # next url's pattern serves urls that didn't match any another
    url(r'^', include('department.urls')),  # if something wrong with urls then don't forget to check this
    url(r'^advertisement/', include('advertisement.urls')),
    url(r'^fact/', include('fact.urls')),
    url(r'^news/', include('news.urls')),
    url(r'^partner/', include('partner.urls')),
    url(r'^technology/', include('technology.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # this too
