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


def slides(request):
    if request.is_ajax():
        return render(request, 'department/slides.html', {'slides': Slide.objects.all().order_by('display_priority')})
