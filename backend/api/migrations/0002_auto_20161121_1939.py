# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-21 19:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lastName', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
                ('firstName', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Task',
        ),
    ]
