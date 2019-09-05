# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import ckeditor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0079_auto_20180622_1056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='advertising',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='广告内容', null=True),
        ),
        migrations.AlterField(
            model_name='carousel',
            name='content',
            field=ckeditor.fields.RichTextField(blank=True, verbose_name='轮播内容', null=True),
        ),
    ]
