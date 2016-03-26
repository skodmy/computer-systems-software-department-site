from django.shortcuts import render
from .models import Partner


def carousel(request):
    partners = Partner.objects.all()[:10]
    context = {'partners': partners}
    return render(request, 'partner/partners_carousel.html', context)
