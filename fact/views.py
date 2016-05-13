from django.shortcuts import render
from django.http import JsonResponse

from fact.models import Fact


def rows(request):
    return render(request, 'fact/rows.html', {'facts': Fact.objects.all()[:3]})


def facts_arguments_json(request):
    context = {}
    for fact in Fact.objects.all()[:3]:
        context.setdefault(fact.id, fact.arguments_json())
    return JsonResponse(context)
