# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-05-19 18:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrlKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key_name', models.CharField(max_length=500, unique=True)),
                ('is_assigned', models.BooleanField(default=False)),
                ('assigned_timestamp', models.DateTimeField(blank=True, null=True)),
                ('assigned_url', models.CharField(blank=True, max_length=500)),
            ],
            options={
                'ordering': ['is_assigned'],
                'verbose_name': 'Url Key',
                'verbose_name_plural': 'Url Keys',
            },
        ),
    ]
