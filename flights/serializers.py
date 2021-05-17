from rest_framework import serializers
from flights.models import Flight


class FlightSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['id', 'name', 'to', 'date', 'hour']
