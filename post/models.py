from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=300, unique=True)

    def __str__(self):
        return '#' + self.name


class Post(models.Model):
    SINGLE_ROOT_URL = 'post-'

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
        print(content_images)
        for content_image in content_images:
            if not self.content.find('src="!image"'):
                return self.content
            self.content = self.content.replace('src="!image"', 'src="' + content_image.file.url + '"', 1)
        return self.content

    def short_description(self):
        return self.content.replace('<p>', '').replace('</p>', '')[:300] + '...'

    def single_url(self):
        return '/post/' + self.SINGLE_ROOT_URL + str(self.id)

    class Meta:
        abstract = True


class PostContentImage(models.Model):
    UPLOAD_TO = 'post'
    file = models.ImageField(upload_to=UPLOAD_TO + '/content_images')
    priority = models.IntegerField(default=0)

    def __str__(self):
        return self.file.name

    class Meta:
        abstract = True


class News(Post):
    SINGLE_ROOT_URL = 'news/article-'

    def collect_content_images(self):
        return NewsContentImage.objects.filter(news=self)

    class Meta:
        verbose_name_plural = 'News'


class NewsContentImage(PostContentImage):
    UPLOAD_TO = 'news'
    news = models.ForeignKey(News)

    def __str__(self):
        return super().__str__() + ' in ' + self.news.title


class Author(models.Model):
    name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.name

    @staticmethod
    def rating_objects(max_objects=5):
        authors_statistics = {author: Attentor.objects.filter(author=author).count() for author in
                              Author.objects.all()}
        authors_rating = [
            author for author, attentor_count in authors_statistics.items()
            for next_greatest_attentor_count in sorted(authors_statistics.values(), reverse=True)
            if attentor_count == next_greatest_attentor_count
        ][:max_objects]
        for i in range(len(authors_rating)):
            authors_rating[i].rating_number = i + 1
        return authors_rating


class Attentor(Post):
    SINGLE_ROOT_URL = 'attentors/attentor-'

    author = models.ForeignKey(Author)
    # TODO add here field is_actual

    def collect_content_images(self):
        return AttentorContentImage.objects.filter(attentor=self)


class AttentorContentImage(PostContentImage):
    UPLOAD_TO = 'attentor'
    attentor = models.ForeignKey(Attentor)

    def __str__(self):
        return super().__str__() + ' in ' + self.attentor.title
