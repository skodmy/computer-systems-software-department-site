from django.shortcuts import render
from django.core.paginator import Paginator
from .models import News, Attentor, Author


NEWS_PER_PAGE = 7
ATTENTORS_PER_PAGE = 8


def create_paginator_context(model_class, objects_per_page, page_url, active_page_number=1):
    context = {
        'paginator': Paginator(model_class.objects.all(), objects_per_page),
        'page_url': page_url
    }
    context.setdefault('active_page', context.get('paginator').page(active_page_number))
    return context


def create_post_context(post_header, post_record_class, post_card_class, single_post_url):
    return {
        'post_header4': post_header,
        'post_record_class': post_record_class,
        'post_card_class': post_card_class,
        'single_post_url': single_post_url
    }


def create_row_posts_block_context(header, posts, single_url):
    return {
        'row_posts_block_header4': header,
        'row_posts': posts,
        'single_row_post_url': single_url
    }


def create_side_posts_block_context(header, posts, single_url):
    return {
        'side_posts_block_header4': header,
        'side_posts': posts,
        'single_side_post_url': single_url
    }


def news(request, page_number):
    context = {'attentors': Attentor.objects.all()[:5],
               'search_form_action': '/'}  # TODO place here search url instead /
    context.update(create_post_context('Новини', 'news-record', 'news-card', 'news/id'))
    context.update(create_paginator_context(News, NEWS_PER_PAGE, '/post/news/page-', page_number))
    return render(request, 'post/news.html', context)


def attentors(request, page_number):
    context = {'search_form_action': '/'}
    context.update(create_post_context('Оголошення', 'attentor-record', 'attentor-card', 'adver/id'))
    context.update(
        create_paginator_context(Attentor, ATTENTORS_PER_PAGE, '/post/attentors/page-',
                                 page_number))
    context.setdefault('authors_rating', Author.rating_objects())
    return render(request, 'post/attentors.html', context)


def news_single_article(request, article_id):
    article = News.objects.get(id=article_id)
    context = {'post': article}
    context.update(create_row_posts_block_context('Останні новини', News.objects.all().order_by('-publication_date_time')[:5],'single-url'))
    context.update(create_side_posts_block_context('Схожі новини',
            News.objects.filter(tags=article.tags.all(),
                publication_date_time=article.publication_date_time).exclude(id=article.id),
    'single-url'))
    return render(request, 'post/news_single_article.html', context)


def attentor(request, attentor_id):
    adv = Attentor.objects.get(id=attentor_id)
    context = {'post': adv}
    context.update(create_row_posts_block_context('Топ оголошення', Attentor.objects.all().order_by('-views')[:5], 'single-url'))
    context.update(create_side_posts_block_context('Інші оголошення цього автора', Attentor.objects.filter(author=adv.author)[:5], 'single-url'))
    return render(request, 'post/attentor.html', context)
