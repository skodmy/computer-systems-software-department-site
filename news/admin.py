from django.contrib import admin

from .models import News, Tag


class NewsAdmin(admin.ModelAdmin):
    pass

admin.site.register(News, NewsAdmin)
admin.site.register(Tag)
