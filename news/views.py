from django.shortcuts import render

from .models import News


def records(request):
    context = {'news_list': News.objects.all()[:5]}
    return render(request, 'news/records.html', context)


def news_details(request):
    return render(request, 'news/news.html')
