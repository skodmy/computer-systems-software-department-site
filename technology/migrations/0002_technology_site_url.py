# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-09-04 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('technology', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='technology',
            name='site_url',
            field=models.URLField(default='http://localhost'),
        ),
    ]
