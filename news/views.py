from django.shortcuts import render
from advertisement.models import Advertisement
from .models import News
from django.core.paginator import Paginator


NEWS_ON_PAGE = 7


def index(request, page):
    context = {'advertisements': Advertisement.objects.all()[:5], 'page_url': '/news/page'}
    paginator = Paginator(News.objects.all(), NEWS_ON_PAGE)
    context.setdefault('paginator', paginator)
    active_page = paginator.page(page)
    context.setdefault('news_list', active_page.object_list)
    context.setdefault('active_page', active_page)
    context.setdefault('search_form_action', '/')  # TODO place here search url instead /
    return render(request, 'news/index.html', context)


def single_news(request, id):
    return render(request, 'news/single-news.html', {'latest_news': News.objects.all()[:3]})


def search(request):
    return render(request, 'news/index.html')
