from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Person(models.Model):
	firstname = models.CharField(max_length=50)
	lastname  = models.CharField(max_length=50)
	midlename = models.CharField(max_length=50)
	birthdate = models.DateTimeField()
	deathdate = models.DateTimeField()

class PersonInfo(models.Model):
	person = models.ForeignKey(Person, on_delete=models.CASCADE)
	info_text = models.CharField(max_length=500)