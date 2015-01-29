# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('short_summary', models.CharField(max_length=100)),
                ('long_summary', models.CharField(max_length=2000)),
                ('url', models.CharField(max_length=200)),
                ('created', models.DateTimeField(default=datetime.datetime(2015, 1, 29, 15, 48, 1, 45000))),
                ('updated', models.DateTimeField(default=datetime.datetime(2015, 1, 29, 15, 48, 1, 45000))),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
