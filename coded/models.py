from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Count, F, Value
from django.db.models.functions import Length, Upper
from django.db.models.lookups import GreaterThan


# Create your models here.
User = get_user_model()

class Event(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField()
    organiser = models.ForeignKey(User,on_delete=models.CASCADE,related_name="events",)
    description = models.TextField()
    datetime = models.DateTimeField()
    location = models.CharField(max_length=150)
    seats = models.PositiveIntegerField()


class Booking(models.Model):
    seats = models.PositiveIntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE,related_name="bookings",)
    data = models.DateField()
    event = models.ForeignKey(Event,on_delete=models.CASCADE,related_name="bookingrevents")

