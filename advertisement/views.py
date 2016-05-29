from django.shortcuts import render

from .models import Advertisement


def cards_list(request):
    context = {'advertisements': Advertisement.objects.filter(is_actual=True)[:5]}
    return render(request, 'advertisement/cards_list.html', context)


def index(request):
    return render(request, 'advertisement/advertisements.html')


def single(request, id):
    return render(request, 'advertisement/single-advertisment.html')