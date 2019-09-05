# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0077_auto_20180621_1713'),
    ]

    operations = [
        migrations.AddField(
            model_name='carousel',
            name='newlink',
            field=models.URLField(verbose_name='轮播推荐文章链接', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='webpurl',
            field=models.URLField(verbose_name='web图片链接地址', blank=True, null=True),
        ),
    ]
