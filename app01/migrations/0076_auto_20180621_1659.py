# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0075_carousel'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='carousel',
            options={'verbose_name': '图片轮播', 'verbose_name_plural': '图片轮播'},
        ),
    ]
