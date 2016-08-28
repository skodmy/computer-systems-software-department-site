from django.contrib import admin
from .models import Advertisement, Author, News, Tag, NewsContentImage, AdvertisementContentImage

admin.site.register(Tag)
admin.site.register(News)
admin.site.register(Author)
admin.site.register(Advertisement)
admin.site.register(NewsContentImage)
admin.site.register(AdvertisementContentImage)
