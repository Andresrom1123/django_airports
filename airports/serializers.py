from rest_framework import serializers

from airports.models import Airport
from planes.serializers import PlaneSerializer


class AirportCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airport
        fields = ['id', 'name', 'city', 'planes']


class AirportSerializer(serializers.ModelSerializer):
    planes = PlaneSerializer(many=True)

    class Meta:
        model = Airport
        fields = ['id', 'name', 'city', 'planes']
