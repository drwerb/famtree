# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-23 09:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='birthdate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='deathdate',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]