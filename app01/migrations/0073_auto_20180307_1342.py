# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0072_auto_20180307_1338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='videourl',
            field=models.TextField(verbose_name='教程URL', null=True, blank=True),
        ),
    ]
