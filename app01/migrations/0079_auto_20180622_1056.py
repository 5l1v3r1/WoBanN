# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0078_auto_20180621_1721'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertising',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True, auto_created=True, verbose_name='ID')),
                ('title', models.CharField(verbose_name='标题', max_length=30)),
                ('summary', models.CharField(null=True, blank=True, verbose_name='简介', max_length=256)),
                ('content', ckeditor.fields.RichTextField(null=True, blank=True, verbose_name='课程内容')),
                ('newlink', models.URLField(null=True, blank=True, verbose_name='广告链接')),
                ('newpic', models.ImageField(upload_to='upload_imgss/', default='upload_imgss/logo.jpg', verbose_name='封面图片(280x125)')),
                ('create_date', models.DateTimeField(auto_now_add=True, verbose_name='发布时间')),
            ],
            options={
                'verbose_name': '广告位',
                'verbose_name_plural': '广告位',
            },
        ),
        migrations.RemoveField(
            model_name='carousel',
            name='webpurl',
        ),
        migrations.AlterField(
            model_name='carousel',
            name='newpic',
            field=models.ImageField(upload_to='upload_imgss/', default='upload_imgss/logo.jpg', verbose_name='封面图片(2360x700)'),
        ),
    ]
