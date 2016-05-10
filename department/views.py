from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .models import Slide


def index(request):
    return render(request, 'department/index.html')


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
    return HttpResponseRedirect('/')


def slides(request):
    if request.is_ajax():
        return render(request, 'department/slides.html', {'slides': Slide.objects.all().order_by('display_priority')})
