from django.db import models

from airports.models import Airport
from planes.models import Plane


class Flight(models.Model):
    name = models.CharField(max_length=100)
    date = models.DateField()
    hour = models.TimeField()
    CITIES_CHOICES = [
        ('GDL', 'Guadalajara'),
        ('MTY', 'Monterrey'),
        ('TJ', 'Tijuana'),
        ('SN', 'Sonora')
    ]
    to = models.CharField(
        max_length=5,
        choices=CITIES_CHOICES
    )
    airports = models.ForeignKey(Airport, related_name='airports_flights', on_delete=models.CASCADE)
    planes = models.ForeignKey(Plane, related_name='planes_flights', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date', 'hour']
