from django.contrib import admin
from .models import Attentor, Author, News, Tag, NewsContentImage, AttentorContentImage

admin.site.register(Tag)
admin.site.register(News)
admin.site.register(Author)
admin.site.register(Attentor)
admin.site.register(NewsContentImage)
admin.site.register(AttentorContentImage)
