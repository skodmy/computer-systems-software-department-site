from django.db import models


class Technology(models.Model):
    name = models.CharField(max_length=75)
    logotype = models.ImageField(upload_to='technology/images')
    site_url = models.URLField(default='http://localhost')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'technologies'
