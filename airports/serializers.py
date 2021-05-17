from rest_framework import serializers

from airports.models import Airport
from flights.serializers import FlightSerializer
from planes.serializers import PlaneSerializer


class AirportCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = ['id', 'name', 'city']


class AirportSerializer(serializers.ModelSerializer):
    flights = FlightSerializer(many=True)
    planes = PlaneSerializer(many=True)

    class Meta:
        model = Airport
        fields = ['id', 'name', 'city', 'planes', 'flights']
