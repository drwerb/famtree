from django.test import TestCase

from inv.models import Person, Relation

class PersonRelationsTests(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.son = Person.objects.create(
            firstname='Jhon',
            lastname='Smith',
            midlename='Agent'
        )

        cls.father = Person.objects.create(
            firstname='Jhon',
            lastname='Smith',
            midlename='Agent'
        )

        cls.mother = Person.objects.create(
            firstname='Jhon',
            lastname='Smith',
            midlename='Agent'
        )

        cls.moms_grandma = Person.objects.create(
            firstname='Jhon',
            lastname='Smith',
            midlename='Agent'
        )

        cls.moms_grandpa = Person.objects.create(
            firstname='Jhon',
            lastname='Smith',
            midlename='Agent'
        )

        Relation.objects.create(person=cls.son, rel_type='parent', related=cls.father)
        Relation.objects.create(person=cls.son, rel_type='parent', related=cls.mother)

        Relation.objects.create(person=cls.father, rel_type='child', related=cls.son)
        Relation.objects.create(person=cls.mother, rel_type='child', related=cls.son)

        Relation.objects.create(person=cls.mother, rel_type='parent', related=cls.moms_grandpa)
        Relation.objects.create(person=cls.mother, rel_type='parent', related=cls.moms_grandma)

        Relation.objects.create(person=cls.moms_grandpa, rel_type='child', related=cls.mother)
        Relation.objects.create(person=cls.moms_grandma, rel_type='child', related=cls.mother)


    def test_intance_creation(self):
        self.assertNotEqual(self.son.id, None)

    def test_relations_count(self):
        self.assertEqual(self.son.relations.all().count(), 2)
        self.assertEqual(self.mother.relations.all().count(), 3)
        self.assertEqual(self.father.relations.all().count(), 1)

    def test_relation_filters(self):
        self.assertEqual(
            Person.objects
                .filter(relations__person=self.mother, relations__rel_type='child')
                .get()
            ,
            self.son
        )
