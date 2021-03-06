# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-06-09 23:56
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
                ('course_name', models.CharField(max_length=250)),
                ('course_logo', models.FileField(upload_to=b'')),
                ('course_description', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='Course_Content',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_content_description', models.CharField(max_length=250)),
                ('course_content1', models.FileField(upload_to=b'')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning.Course')),
            ],
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question_title', models.CharField(max_length=250)),
                ('question_description', models.FileField(upload_to=b'')),
                ('question_option1', models.CharField(max_length=250)),
                ('question_option2', models.CharField(max_length=250)),
                ('question_option3', models.CharField(max_length=250)),
                ('question_option4', models.CharField(max_length=250)),
                ('question_hint1', models.CharField(max_length=250)),
                ('question_explanation', models.CharField(max_length=250)),
                ('question_difficulty', models.CharField(max_length=250)),
                ('hint_taken', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quiz_description', models.CharField(max_length=250)),
                ('numOfQuestions', models.CharField(max_length=250)),
                ('course_content', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning.Course_Content')),
            ],
        ),
        migrations.CreateModel(
            name='Quiz_Performance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('noOfQuestionsCorrect', models.CharField(max_length=250)),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning.Quiz')),
                ('user', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='learning.Quiz'),
        ),
    ]
