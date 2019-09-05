# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0069_auto_20180128_1236'),
    ]

    operations = [
        migrations.AddField(
            model_name='documentdata',
            name='newpic_webp',
            field=models.ImageField(verbose_name='封面图片.webp', upload_to='upload_imgss/', default='upload_imgss/logo.jpg'),
        ),
        migrations.AddField(
            model_name='news',
            name='newpic_webp',
            field=models.ImageField(verbose_name='封面图片.webp', upload_to='upload_imgss/', default='upload_imgss/logo.jpg'),
        ),
    ]
