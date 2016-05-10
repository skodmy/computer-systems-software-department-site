from django.db import models
from department.models import SlideCreationModel


class News(SlideCreationModel):
    heading = models.CharField(max_length=150)
    image = models.ImageField(upload_to='news/images', null=True, blank=True) # TODO Are that null & blank good?
    short_description = models.TextField(max_length=300)
    publication_date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.heading

    def create_slide_from(self):
        self.create_slide(display_priority=0, big_slogan=self.heading, small_slogan='', background_image=self.image, action_href='#')
