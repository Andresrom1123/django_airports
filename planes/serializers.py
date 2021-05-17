from rest_framework import serializers

from flights.serializers import FlightSerializer
from planes.models import Plane


class PlaneCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plane
        fields = ['id', 'name']


class PlaneSerializer(serializers.ModelSerializer):
    flights = FlightSerializer(many=True)

    class Meta:
        model = Plane
        fields = ['id', 'name', 'flights']
