# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0058_auto_20171230_0740'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentdata',
            name='newpic',
            field=models.ImageField(upload_to='uploadImages', verbose_name='封面图片', default='medias/upload_imgss/logo.jpg'),
        ),
    ]
