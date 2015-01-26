from django.db import models

# Create your models here.


class Publisher(models.Model):
    name = models.CharField(max_length=50)
    city = models.CharField(max_length=10)
    address= models.CharField(max_length=100)
    state_province = models.CharField(max_length=10)
    country = models.CharField(max_length=10)
    website = models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField()

    def __unicode__(self):
        return self.first_name + ' ' +self.last_name


class Book(models.Model):
    title = models.CharField(max_length=50)
    publisher = models.ForeignKey(Publisher)
    author = models.ManyToManyField(Author)
    publication_date = models.DateField()

    def __unicode__(self):
        return self.title


