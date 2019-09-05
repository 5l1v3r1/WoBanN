# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0074_auto_20180307_1352'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('title', models.CharField(verbose_name='标题', max_length=30)),
                ('summary', models.CharField(blank=True, null=True, max_length=256, verbose_name='简介')),
                ('content', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='课程内容')),
                ('newpic', models.ImageField(verbose_name='封面图片', default='upload_imgss/logo.jpg', upload_to='upload_imgss/')),
                ('newpic_webp', models.ImageField(verbose_name='封面图片.webp', default='upload_imgss/logo.jpg', upload_to='upload_imgss/')),
                ('create_date', models.DateTimeField(verbose_name='发布时间', auto_now_add=True)),
                ('category', models.ForeignKey(to='app01.Category', blank=True, null=True)),
                ('user', models.ForeignKey(to='app01.Admin')),
            ],
            options={
                'verbose_name': '视频教程',
                'verbose_name_plural': '视频教程',
            },
        ),
    ]
