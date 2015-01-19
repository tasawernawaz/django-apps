# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20150115_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 19, 16, 16, 59, 364000)),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 19, 16, 16, 59, 364000)),
        ),
    ]
