from django.db import models


class Partner(models.Model):
    name = models.CharField(max_length=75)
    logotype = models.ImageField(upload_to='partner/images')
    site_url = models.URLField()

    def __str__(self):
        return self.name
