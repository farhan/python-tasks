# Generated by Django 2.2.3 on 2020-05-01 11:06

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0004_movie_movie_trailer'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2020, 5, 1, 11, 6, 37, 749660, tzinfo=utc)),
        ),
    ]