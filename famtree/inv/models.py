from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Person(models.Model):
    firstname = models.CharField(max_length = 50)
    lastname  = models.CharField(max_length = 50)
    midlename = models.CharField(max_length = 50)
    birthdate = models.DateTimeField(null = True, blank = True)
    deathdate = models.DateTimeField(null = True, blank = True)

    def __str__(self):
        return (self.lastname + " " + self.firstname + " " + self.midlename).encode('utf8', errors = 'replace')

class PersonInfo(models.Model):
    person = models.ForeignKey(Person, on_delete = models.CASCADE)
    info_text = models.CharField(max_length = 500)
