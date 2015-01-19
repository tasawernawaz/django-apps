# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 15, 18, 1, 10, 734000)),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='updated',
            field=models.DateTimeField(default=datetime.datetime(2015, 1, 15, 18, 1, 10, 734000)),
        ),
        migrations.AlterField(
            model_name='tasks',
            name='url',
            field=models.CharField(max_length=100),
        ),
    ]
