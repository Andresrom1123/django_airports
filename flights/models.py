from django.db import models


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

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-date', 'hour']
