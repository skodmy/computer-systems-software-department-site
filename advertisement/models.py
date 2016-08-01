from django.db import models

from news.models import Tag


class Advertisement(models.Model):
    title = models.CharField(max_length=100)
    main_message = models.TextField(max_length=300)
    published_date_time = models.DateTimeField(auto_now_add=True)
    is_actual = models.BooleanField(default=True)
    image = models.ImageField(upload_to='advertisement/images', null=True, blank=True)
    author = models.CharField(max_length=200, default='Анонім')
    views = models.IntegerField(default=0)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.title + ' ' + self.author
