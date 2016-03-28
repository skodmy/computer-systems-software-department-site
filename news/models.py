from django.db import models


class News(models.Model):
    heading = models.CharField(max_length=150)
    image = models.ImageField(upload_to='news/images', null=True, blank=True) # TODO Are that null & blank good?
    short_description = models.TextField(max_length=300)
    publication_date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.heading
