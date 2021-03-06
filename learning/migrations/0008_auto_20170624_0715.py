# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-06-24 07:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0007_quiz_performance_numofquestions'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='noOfQuestionsAttempted',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='noOfQuestionsCorrect',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='quiz',
            name='question_wrong1',
            field=models.CharField(default=0, max_length=250),
            preserve_default=False,
        ),
    ]
