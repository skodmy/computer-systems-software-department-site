from django.shortcuts import render

from .models import Technology


def divs_list(request):
    context = {'technologies': Technology.objects.all()}
    return render(request, 'technology/divs_list.html', context)
