# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-10-08 22:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('four', '0004_dept_emp'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bird',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('color', models.CharField(max_length=32)),
            ],
            options={
                'db_table': 'bird',
            },
        ),
    ]
