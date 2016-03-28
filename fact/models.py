from django.db import models


class Fact(models.Model):
    text = models.CharField(max_length=300)
    number = models.SmallIntegerField(default=-1)
    is_percentage = models.BooleanField(default=False)

    def __str__(self):
        result = self.text
        if self.number == -1:
            return result
        result = str(self.number) + '% ' + result if self.is_percentage else str(self.number) + ' ' + result
        return result
