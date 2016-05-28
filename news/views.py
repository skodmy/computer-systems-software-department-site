from django.shortcuts import render

from advertisement.models import Advertisement
from .models import News


def index(request):
    return render(request, 'news/index.html', {'news_list': News.objects.all(),
                                               'advertisements': Advertisement.objects.all()[:5]})


def single_news(request, id):
    return render(request, 'news/single-news.html', {'latest_news': News.objects.all()[:3]})


def search(request):
    return render(request, 'news/index.html')
