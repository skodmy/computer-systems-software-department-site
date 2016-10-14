# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-10-14 10:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_record', models.CharField(max_length=10)),
                ('academic_index', models.IntegerField()),
                ('research_index', models.IntegerField()),
                ('social_activities', models.IntegerField()),
                ('together', models.IntegerField()),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Course')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Year_of_accession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Year_of_study',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='students',
            name='year_of_accession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Year_of_accession'),
        ),
        migrations.AddField(
            model_name='students',
            name='year_of_study',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.Year_of_study'),
        ),
    ]
