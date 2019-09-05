# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0047_auto_20171220_1536'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='videourls',
        ),
        migrations.AddField(
            model_name='news',
            name='url',
            field=models.URLField(null=True, verbose_name='链接地址', blank=True, default='www.askeds.com/server'),
        ),
    ]
