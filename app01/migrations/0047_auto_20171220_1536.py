# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0046_auto_20171210_1549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='url',
        ),
        migrations.AddField(
            model_name='news',
            name='videourls',
            field=models.CharField(verbose_name='课程列表', max_length=5000, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='admin',
            name='userpic',
            field=models.ImageField(verbose_name='头像', default='medias/images/image30.png', upload_to='medias/images/'),
        ),
        migrations.AlterField(
            model_name='documentdata',
            name='document_data',
            field=models.FileField(verbose_name='文档资料', default='medias/document/20170209130422_Broods.txt', upload_to='medias/document/'),
        ),
        migrations.AlterField(
            model_name='documentdata',
            name='newpic',
            field=models.ImageField(verbose_name='封面图片', default='medias/upload_imgss/logo.jpg', upload_to='medias/upload_imgss/'),
        ),
        migrations.AlterField(
            model_name='news',
            name='newpic',
            field=models.ImageField(verbose_name='封面图片', default='medias/upload_imgss/logo.jpg', upload_to='medias/images/'),
        ),
        migrations.AlterField(
            model_name='news',
            name='video',
            field=models.FileField(verbose_name='教程(.mp3 .mp4)', null=True, blank=True, upload_to='medias/video/'),
        ),
    ]
