from django.shortcuts import render

from .models import News


def cards_list(request):
    context = {'news_list': News.objects.all()[:5]}
    return render(request, 'news/cards_list.html', context)
