# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0073_auto_20180307_1342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='videos_url',
            field=models.TextField(blank=True, verbose_name='课程列表', null=True),
        ),
        migrations.AlterField(
            model_name='news',
            name='videourl',
            field=models.CharField(blank=True, verbose_name='教程URL', max_length=5000, null=True),
        ),
    ]
