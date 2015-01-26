# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20150119_1616'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 20, 11, 9, 31, 424000)),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='long_summary',
            field=models.CharField(max_length=2000),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 20, 11, 9, 31, 424000)),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='url',
            field=models.CharField(max_length=200),
        ),
    ]
