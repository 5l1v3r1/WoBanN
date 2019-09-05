# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0048_auto_20171220_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='videos_url',
            field=models.CharField(verbose_name='课程列表', null=True, max_length=5000, blank=True),
        ),
    ]
