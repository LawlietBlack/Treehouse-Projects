# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-12 00:49
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20160208_1716'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Step',
            new_name='Text',
        ),
    ]