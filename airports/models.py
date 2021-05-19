from django.db import models

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
    planes = models.ManyToManyField(Plane, related_name='airports_plane')

    def __str__(self):
        return self.name
