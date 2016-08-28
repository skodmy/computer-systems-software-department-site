from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=300, unique=True)

    def __str__(self):
        return '#' + self.name


class Post(models.Model):
    title = models.CharField(max_length=300)
    front_image = models.ImageField(upload_to='post/front_images', blank=True, null=True)
    content = models.TextField(blank=True, null=True)
    views = models.IntegerField(default=0)
    tags = models.ManyToManyField(Tag, blank=True)
    publication_date_time = models.DateTimeField(auto_now_add=True)
    last_modification_date_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def collect_content_images(self):
        raise NotImplementedError

    def render_content(self):
        content_images = self.collect_content_images().order_by('priority')
        for content_image in content_images:
            if not self.content.find('src="!image"'):
                return self.content
            self.content = self.content.replace('src="!image"', 'src="' + content_image.url + '"')
        return self.content

    class Meta:
        abstract = True


class PostContentImage(models.Model):
    UPLOAD_TO = 'post'
    file = models.ImageField(upload_to=UPLOAD_TO + '/content_images')
    priority = models.IntegerField(default=0)

    def __str__(self):
        return self.post.title

    class Meta:
        abstract = True


class News(Post):
    def collect_content_images(self):
        return NewsContentImage.objects.filter(news=self)


class NewsContentImage(PostContentImage):
    UPLOAD_TO = 'news'
    news = models.ForeignKey(News)


class Author(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name


class Advertisement(Post):
    author = models.ForeignKey(Author)

    def collect_content_images(self):
        return AdvertisementContentImage.objects.filter(advertisement=self)


class AdvertisementContentImage(PostContentImage):
    UPLOAD_TO = 'advertisement'
    advertisement = models.ForeignKey(Advertisement)
