from django.db import models


# Create your models here.
class Slide(models.Model):
    display_priority = models.SmallIntegerField()
    big_slogan = models.CharField(max_length=200)
    small_slogan = models.CharField(max_length=200)
    background_image = models.ImageField(upload_to='department/images/slider')
    action_href = models.CharField(max_length=200)

    def __str__(self):
        return self.big_slogan + ' ' + self.small_slogan


class SlideCreationModel(models.Model):
    create_slide_on_save = models.BooleanField(default=False)

    create_slide = Slide.objects.create

    def create_slide_from(self):
        raise NotImplementedError()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        if self.create_slide_on_save:
            self.create_slide_from()
            self.create_slide_on_save = False
        super().save(force_insert, force_update, using, update_fields)

    class Meta:
        abstract = True
