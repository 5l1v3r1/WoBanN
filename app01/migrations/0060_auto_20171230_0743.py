# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0059_auto_20171230_0741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentdata',
            name='newpic',
            field=models.ImageField(verbose_name='封面图片', default='medias/upload_imgss/logo.jpg', upload_to='medias/upload_imgss/'),
        ),
    ]
