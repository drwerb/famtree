from neo4django.db import models

class Person(models.NodeModel):
    db_id = models.StringProperty()

    mother = models.Relationship('self', rel_type='mother', single=True, related_name='child')
    father = models.Relationship('self', rel_type='father', single=True, related_name='child')
    married_to = models.Relationship('self', rel_type='married_to', related_name='child')
