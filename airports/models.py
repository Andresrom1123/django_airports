from django.db import models

from flights.models import Flight
from planes.models import Plane


class Airport(models.Model):
    name = models.CharField(max_length=100)
    CITIES_CHOICES = [
        ('GDL', 'Guadalajara'),
        ('MTY', 'Monterrey'),
        ('TJ', 'Tijuana'),
        ('SN', 'Sonora')
    ]
    city = models.CharField(
        max_length=5,
        choices=CITIES_CHOICES
    )
    flights = models.ManyToManyField(Flight, related_name='airports_flights')
    planes = models.ManyToManyField(Plane, related_name='airports_plane')
