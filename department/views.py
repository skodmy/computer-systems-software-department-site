from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from .models import Slide
from post.models import News, Attentor
from technology.models import Technology
from partner.models import Partner
from post.views import ATTENTORS_PER_PAGE, NEWS_PER_PAGE, create_row_posts_block_context, \
    create_side_posts_block_context


def index(request):
    context = {'slides': Slide.objects.all().order_by('display_priority')}
    context.setdefault('technologies', Technology.objects.all())
    context.setdefault('news', News.objects.all()[:NEWS_PER_PAGE])
    context.setdefault('partners', Partner.objects.all())
    context.setdefault('attentors', Attentor.objects.all()[:ATTENTORS_PER_PAGE])
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
    context = create_row_posts_block_context('Топ оголошення', Attentor.objects.all()[:5],'single-url')
    context.update(create_side_posts_block_context('Останні новини',
                                                   News.objects.all().order_by('-publication_date_time')[:5],
                                                   'single-url'))
    return render(request, 'department/contacts.html', context)


def applicant_in_general(request):
    return render(request, 'department/applicant_in_general.html',
                  create_row_posts_block_context('Останні новини',
                                                 News.objects.all().order_by('-publication_date_time')[:5], 'single-url'))


def about_specialization(request):
    return render(request, 'department/about_specialization.html',
                  create_row_posts_block_context('Останні новини',
                                                News.objects.all().order_by('-publication_date_time')[:5], 'single-url'))


def academic_subjects(request):
    return render(request, 'department/academic_subjects.html',
                  create_row_posts_block_context('Останні новини',
                                                 News.objects.all().order_by('-publication_date_time')[:5],
                                                 'single-url'))


def useful_links(request):
    return render(request, 'department/useful_links.html',
                  create_row_posts_block_context('Останні новини',
                                                 News.objects.all().order_by('-publication_date_time')[:5],
                                                 'single-url'))


def students_rating(request):
    return render(request, 'department/students_rating.html',
                  create_row_posts_block_context('Останні новини',
                                                 News.objects.all().order_by('-publication_date_time')[:5],
                                                 'single-url'))


def lessons_schedule(request):
    return render(request, 'department/lessons_schedule.html',
                  create_row_posts_block_context('Останні новини',
                                                 News.objects.all().order_by('-publication_date_time')[:5],
                                                 'single-url'))


def under_development(request):
    return render(request, 'department/under_development.html')
