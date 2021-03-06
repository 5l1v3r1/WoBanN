# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-09-05 08:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0007_auto_20170904_1105'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='videourl',
            field=models.URLField(blank=True, default='', null=True, verbose_name='百度云盘URL'),
        ),
        migrations.AlterField(
            model_name='news',
            name='video',
            field=models.FileField(default='', upload_to='statics/video/', verbose_name='教程(.mp3 .mp4)'),
        ),
    ]
