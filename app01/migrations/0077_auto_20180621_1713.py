# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0076_auto_20180621_1659'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='carousel',
            name='category',
        ),
        migrations.RemoveField(
            model_name='carousel',
            name='newpic_webp',
        ),
        migrations.RemoveField(
            model_name='carousel',
            name='user',
        ),
        migrations.AddField(
            model_name='carousel',
            name='webpurl',
            field=models.URLField(blank=True, null=True, verbose_name='链接地址'),
        ),
    ]
