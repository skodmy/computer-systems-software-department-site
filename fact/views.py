from django.shortcuts import render

from fact.models import Fact


def divs_list(request):
    context = {'facts':Fact.objects.all()[:5]}
    return render(request, 'fact/divs_list.html', context)
