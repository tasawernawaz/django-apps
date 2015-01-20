
from datetime import datetime
from django.contrib.auth.models import User
from django.db import models


class Tasks(models.Model):
    user = models.ForeignKey(User)
    short_summary = models.CharField(max_length=100)
    long_summary = models.CharField(max_length=2000)
    url = models.CharField(max_length=200)
    created = models.DateTimeField(default=datetime.now())
    updated = models.DateTimeField(default=datetime.now())