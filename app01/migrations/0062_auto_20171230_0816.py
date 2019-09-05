# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0061_auto_20171230_0815'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentdata',
            name='document_data',
            field=models.FileField(upload_to='medias/document/', verbose_name='文档资料', default='medias/document/20170209130422_Broods.txt'),
        ),
        migrations.AlterField(
            model_name='documentdata',
            name='newpic',
            field=models.ImageField(upload_to='medias/upload_imgss/', verbose_name='封面图片', default='medias/upload_imgss/logo.jpg'),
        ),
    ]
