from django.db import models

# Create your models here.

CATEGORY_CHOICES = (
    ('action', 'ACTION'),
    ('drama', 'DRAMA'),
    ('comedy', 'COMEDY'),
    ('romance', 'ROMANCE'),
)

LANGUAGE_CHOICES = (
    ('english', 'ENGLISH'),
    ('german', 'GERMAN'),
)

STATUS_CHOICES = (
    ('RA', 'RECRNTLY ADDED'),
    ('MW', 'MOST WATCHED'),
    ('TR', 'TOP RATED'),
)


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='movies')
    banner = models.ImageField(upload_to='movies_banner')
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=10)
    language = models.CharField(choices=LANGUAGE_CHOICES, max_length=10)
    status = models.CharField(choices=STATUS_CHOICES, max_length=2)
    cast = models.CharField(max_length=100)
    year_of_production = models.DateField()
    views_count = models.IntegerField(default=0)
