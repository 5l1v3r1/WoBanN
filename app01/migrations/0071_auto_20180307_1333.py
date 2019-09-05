# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0070_auto_20180128_1300'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='videourl',
            field=models.CharField(verbose_name='教程URL', null=True, max_length=50000, blank=True),
        ),
    ]
