# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-10-09 23:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('four', '0005_bird'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='dept',
            table='Dept',
        ),
        migrations.AlterModelTable(
            name='emp',
            table='Emp',
        ),
    ]
