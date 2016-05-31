# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-31 13:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=100, verbose_name='label')),
                ('priority', models.CharField(max_length=10, verbose_name='priority level')),
                ('number', models.PositiveIntegerField()),
            ],
        ),
    ]