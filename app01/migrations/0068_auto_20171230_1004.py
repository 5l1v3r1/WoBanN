# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0067_auto_20171230_0842'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='userpic',
            field=models.ImageField(default='images/image30.png', verbose_name='头像', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='documentdata',
            name='document_data',
            field=models.FileField(default='document/20170209130422_Broods.txt', verbose_name='文档资料', upload_to='document/'),
        ),
        migrations.AlterField(
            model_name='news',
            name='newpic',
            field=models.ImageField(default='upload_imgss/logo.jpg', verbose_name='封面图片', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='news',
            name='video',
            field=models.FileField(verbose_name='教程(.mp3 .mp4)', upload_to='video/', blank=True, null=True),
        ),
    ]
