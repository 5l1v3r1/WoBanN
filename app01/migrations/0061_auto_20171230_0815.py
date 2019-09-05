# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0060_auto_20171230_0743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documentdata',
            name='document_data',
            field=models.FileField(default='document/20170209130422_Broods.txt', upload_to='document/', verbose_name='文档资料'),
        ),
        migrations.AlterField(
            model_name='documentdata',
            name='newpic',
            field=models.ImageField(default='upload_imgss/logo.jpg', upload_to='upload_imgss/', verbose_name='封面图片'),
        ),
    ]
