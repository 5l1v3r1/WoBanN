# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0065_auto_20171230_0831'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentdata',
            name='newpic',
            field=models.ImageField(default='image/logo.jpg', verbose_name='封面图片', upload_to='image/%Y/%m'),
        ),
    ]
