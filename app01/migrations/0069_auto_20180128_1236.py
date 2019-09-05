# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0068_auto_20171230_1004'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='newpic',
            field=models.ImageField(upload_to='upload_imgss/', default='upload_imgss/logo.jpg', verbose_name='封面图片'),
        ),
    ]
