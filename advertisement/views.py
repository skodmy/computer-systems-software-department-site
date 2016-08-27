from django.shortcuts import render
from .models import Advertisement
from django.core.paginator import Paginator


ADVERTISEMENTS_ON_PAGE = 8


def index(request, page):
    paginator = Paginator(Advertisement.objects.all(), ADVERTISEMENTS_ON_PAGE)
    context = {'paginator': paginator}
    context.setdefault('active_page', paginator.page(page))
    context.setdefault('page_url', '/advertisement/page')
    # TODO place here code to set author rating context
    return render(request, 'advertisement/advertisements.html', context)


def single(request, id):
    return render(request, 'advertisement/single-advertisment.html')

