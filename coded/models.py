from django.db import models

# Create your models here.


class Event(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField()
    description = models.TextField()
    datetime = models.DateTimeField()
    location = models.CharField(max_length=150)
    seats = models.IntegerField()
