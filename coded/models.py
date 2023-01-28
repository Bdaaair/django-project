from django.db import models

# Create your models here.


class Event(models.Model):
    name = models.CharField(max_length=150)
    image = models.ImageField()
    organiser = models.CharField(max_length=150)
    Date = models.DateField()
    title = models.CharField(max_length=100)
    body = models.TextField()
