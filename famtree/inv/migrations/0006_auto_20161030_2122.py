# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-30 21:22
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inv', '0005_auto_20161030_2118'),
    ]

    operations = [
        migrations.RenameField(
            model_name='relation',
            old_name='rel_person',
            new_name='person',
        ),
    ]
