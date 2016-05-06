from django.shortcuts import render

from .models import Technology


def carousel_items_list(request):
    context = {'technologies': Technology.objects.all()}
    return render(request, 'technology/carousel_items_list.html', context)
