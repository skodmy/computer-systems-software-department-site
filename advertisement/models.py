from django.db import models


class Advertisement(models.Model):
    title = models.CharField(max_length=100)
    main_message = models.TextField(max_length=300)
    published_date_time = models.DateTimeField(auto_now_add=True)
    is_actual = models.BooleanField(default=True)

    def __str__(self):
        return self.title
