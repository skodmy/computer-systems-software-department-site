from django.shortcuts import render
from django.core.paginator import Paginator
from .models import News, Advertisement, Author

NEWS_PER_PAGE = 7
ADVERTISEMENTS_PER_PAGE = 8


def create_paginator_context(model_class, objects_per_page, page_url, active_page_number=1):
    context = {'paginator': Paginator(model_class.objects.all(), objects_per_page), 'page_url': page_url}
    context.setdefault('active_page', context.get('paginator').page(active_page_number))
    return context


def create_post_context(post_header, post_record_class, post_card_class, single_post_url):
    return {'post_header4': post_header, 'post_record_class': post_record_class, 'post_card_class': post_card_class,
            'single_post_url': single_post_url}


def news(request, page_number):
    context = {'advertisements': Advertisement.objects.all()[:5],
               'search_form_action': '/'}  # TODO place here search url instead /
    context.update(create_post_context('Новини', 'news-record', 'news-card', 'news/id'))
    context.update(create_paginator_context(News, NEWS_PER_PAGE, '/post/news/page-', page_number))
    return render(request, 'post/news.html', context)


def advertisements(request, page_number):
    context = {'search_form_action': '/'}
    context.update(create_post_context('Оголошення', 'advertisement-record', 'advertisement-card', 'adver/id'))
    context.update(
        create_paginator_context(Advertisement, ADVERTISEMENTS_PER_PAGE, '/post/advertisements/page-',
                                 page_number))
    context.setdefault('authors_rating', Author.rating_objects())
    return render(request, 'post/advertisements.html', context)
