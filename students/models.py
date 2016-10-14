
from django.db import models

from django.contrib.auth.models import User


class Year_of_accession(models.Model):

    year = models.CharField( max_length=10)

    def __unicode__(self):
        return u'%s' % self.year


class Year_of_study(models.Model):

    year = models.CharField(max_length=10)

    def __unicode__(self):
        return u'%s' % self.year


class Course(models.Model):

    course = models.IntegerField()

    def __unicode__(self):
        return u'%s' % self.course


class Students(models.Model):

    user = models.ForeignKey(User, null=True)

    year_of_accession = models.ForeignKey(Year_of_accession)

    year_of_study = models.ForeignKey(Year_of_study)

    course = models.ForeignKey(Course)

    id_record = models.CharField( max_length=10)

    academic_index = models.IntegerField()

    research_index = models.IntegerField()

    social_activities = models.IntegerField()

    together = models.IntegerField()

    def __unicode__(self):
        return u'%s' % self.user
