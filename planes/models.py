from django.db import models

from flights.models import Flight


class Plane(models.Model):
    name = models.CharField(max_length=100)
    flights = models.ManyToManyField(Flight, related_name='plane_flights', blank=True)

    def __str__(self):
        return self.name
