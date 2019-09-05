# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0056_news_videos_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='videos_url',
            field=models.CharField(null=True, blank=True, verbose_name='课程列表', max_length=5000),
        ),
        migrations.AlterField(
            model_name='news',
            name='videourl',
            field=models.CharField(null=True, blank=True, verbose_name='教程URL', max_length=5000),
        ),
    ]
