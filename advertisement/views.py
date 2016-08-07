from django.shortcuts import render

from .models import Advertisement

from django.core.paginator import Paginator


def index(request):
    paginator = Paginator(Advertisement.objects.all(), 3)
    context = {'paginator': paginator}
    context.setdefault('first_page', paginator.page(1))
    return render(request, 'advertisement/advertisements.html', context)


def single(request, id):
    return render(request, 'advertisement/single-advertisment.html')


def page(request, number):
    return render(request, 'advertisement/records_list.html',
                  {'page': Paginator(Advertisement.objects.all(), 3).page(number)})
