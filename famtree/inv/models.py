from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Person(models.Model):
    firstname = models.CharField(max_length = 50)
    lastname  = models.CharField(max_length = 50)
    midlename = models.CharField(max_length = 50)
    birthdate = models.DateTimeField(null = True, blank = True)
    deathdate = models.DateTimeField(null = True, blank = True)
    relations = models.ManyToManyField('self', through='Relation', symmetrical=False)

    def __str__(self):
        return (self.lastname + " " + self.firstname + " " + self.midlename).encode('utf8', errors = 'replace')

class PersonInfo(models.Model):
    person = models.ForeignKey(Person, on_delete = models.CASCADE)
    info_text = models.CharField(max_length = 500)

class Relation(models.Model):
    RELATION_TYPES = (
        ('parent', 'Parent'),
        ('sibling', 'Sibling'),
        ('child', 'Child'),
        ('step_parent', 'Step parent'),
        ('step_sibling', 'Step sibling'),
        ('step_child', 'Step child'),
        ('marriage', 'Marriage'),
        ('divorce', 'Divorce'),
    )
    person = models.ForeignKey(Person, on_delete=models.CASCADE, related_name="relation_from")
    rel_type = models.CharField(max_length=20, choices=RELATION_TYPES)
    related = models.ForeignKey(Person, related_name="relation_to")

