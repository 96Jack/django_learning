# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2020-09-15 14:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('four', '0002_auto_20200914_2130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('s_grade', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='four.Grade')),
            ],
        ),
        migrations.AlterField(
            model_name='four',
            name='name',
            field=models.CharField(max_length=32),
        ),
    ]
