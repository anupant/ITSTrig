# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-06-26 08:25
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('learning', '0011_courseperformancehistory'),
    ]

    operations = [
        migrations.CreateModel(
            name='QuizPerformanceHistory',
            fields=[
                ('quiz_no', models.CharField(max_length=250, primary_key=True, serialize=False)),
                ('numOfQuestions', models.CharField(max_length=250)),
                ('noOfQuestionsCorrect', models.CharField(max_length=250)),
                ('noOfQuestionsAttempted', models.CharField(max_length=250)),
                ('numOfQuestionsWrong', models.CharField(max_length=250)),
                ('quiz_question_hintTaken', models.CharField(max_length=250)),
                ('quiz_question_wrongNo', models.CharField(max_length=250)),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
