from django.shortcuts import render
from advertisement.models import Advertisement
from .models import News
from django.core.paginator import Paginator


def index(request, page=1):
    context = {'advertisements': Advertisement.objects.all()[:5]}
    paginator = Paginator(News.objects.all(),3)
    context.setdefault('paginator', paginator)
    active_page = paginator.page(page)
    context.setdefault('news_list', active_page.object_list)
    context.setdefault('active_page', active_page)
    return render(request, 'news/index.html', context)


def single_news(request, id):
    return render(request, 'news/single-news.html', {'latest_news': News.objects.all()[:3]})


def search(request):
    return render(request, 'news/index.html')


def toggle_page(request, page_number):
    return render(request, 'news/news_list.html', {'news_list': Paginator(News.objects.all(), 3).page(page_number)})
