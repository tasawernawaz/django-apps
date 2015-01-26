from django.db import models

# Create your models here.

class persons_contact(models.Model):
    name = models.CharField(max_length=20)
    phone_no = models.CharField(max_length=11, null=True, blank=True)
    city = models.CharField(max_length=10)
    address = models.CharField(max_length=100)

