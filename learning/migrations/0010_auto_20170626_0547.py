# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-06-26 05:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0009_auto_20170624_0720'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz_performance',
            name='id',
        ),
        migrations.AlterField(
            model_name='quiz_performance',
            name='quiz_no',
            field=models.CharField(max_length=250, primary_key=True, serialize=False),
        ),
    ]
