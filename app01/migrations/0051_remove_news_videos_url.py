# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0050_auto_20171220_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='videos_url',
        ),
    ]
