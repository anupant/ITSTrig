# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-06-15 00:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0002_question1'),
    ]

    operations = [
        migrations.CreateModel(
            name='CoursePerformance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_attempted', models.CharField(max_length=250)),
                ('quiz_question_wrong', models.CharField(max_length=250)),
                ('quiz_question_hintTaken', models.CharField(max_length=250)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning.Course')),
            ],
        ),
    ]
