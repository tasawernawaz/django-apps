# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tasks_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 29, 15, 49, 55, 202000)),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 29, 15, 49, 55, 202000)),
        ),
    ]
