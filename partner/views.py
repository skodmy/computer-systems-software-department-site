from django.shortcuts import render
from .models import Partner


def carousel_items_list(request):
    partners = Partner.objects.all()[:10]
    context = {'partners': partners}
    return render(request, 'partner/carousel_items_list.html', context)
