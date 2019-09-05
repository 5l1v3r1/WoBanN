# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0071_auto_20180307_1333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='videourl',
            field=models.TextField(blank=True, null=True, max_length=50000, verbose_name='教程URL'),
        ),
    ]
