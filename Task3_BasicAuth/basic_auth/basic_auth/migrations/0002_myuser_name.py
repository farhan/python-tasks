# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-24 14:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basic_auth', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='name',
            field=models.CharField(default='Farhan Khan', max_length=30),
            preserve_default=False,
        ),
    ]
