# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0054_news_videos_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='videos_url',
        ),
    ]
