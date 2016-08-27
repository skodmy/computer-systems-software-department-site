from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .models import Slide
from news.models import News
from technology.models import Technology
from partner.models import Partner
from advertisement.models import Advertisement
from news.views import NEWS_ON_PAGE
from advertisement.views import ADVERTISEMENTS_ON_PAGE

def index(request):
    context = {'slides': Slide.objects.all().order_by('display_priority')}
    context.setdefault('technologies', Technology.objects.all())
    context.setdefault('news_list', News.objects.all()[:NEWS_ON_PAGE])
    context.setdefault('partners', Partner.objects.all())
    context.setdefault('advertisements', Advertisement.objects.all()[:ADVERTISEMENTS_ON_PAGE])
    return render(request, 'department/index.html', context)


def ajax_login(request):
    if request.is_ajax():
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        json_response_data = {'exists': False, 'is_active': False}
        if user is not None:
            json_response_data['exists'] = True
            if user.is_active:
                login(request, user)
                if not request.POST.get('remember_user', False):
                    # If value is 0, the user’s session cookie will expire when the user’s Web browser is closed.
                    request.session.set_expiry(0)
                json_response_data['is_active'] = True
                json_response_data.setdefault('username', username)
            else:
                pass
        else:
            pass
        return JsonResponse(json_response_data)
    return HttpResponseRedirect('/')


def manual_logout(request):
    logout(request)
    return JsonResponse({}) if request.is_ajax() else HttpResponseRedirect('/')


def contacts(request):
    return render(request, 'department/contacts.html', {'latest_news': News.objects.all()[:5]})


def applicant_in_general(request):
    return render(request, 'department/applicant_in_general.html', {'latest_news': News.objects.all()[:5]})


def about_specialization(request):
    return render(request, 'department/about_specialization.html', {'latest_news': News.objects.all()[:5]})


def under_development(request):
    return render(request, 'department/under_development.html')
