from django.shortcuts import render

from .models import Advertisement


def actual_cards_list(request):
    context = {'advertisements': Advertisement.objects.filter(is_actual=True)[:5]}
    return render(request, 'advertisement/cards_list.html', context)
