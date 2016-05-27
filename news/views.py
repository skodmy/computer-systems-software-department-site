from django.shortcuts import render

from .models import News


def index(request):
    return render(request, 'news/index.html', {'news_list': News.objects.all()})
