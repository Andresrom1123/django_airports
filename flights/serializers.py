from datetime import datetime

from django.db.models import Q
from rest_framework import serializers

from airports.serializers import AirportSerializer
from flights.models import Flight
from planes.serializers import PlaneSerializer


class FlightCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Flight
        fields = ['id', 'name', 'to', 'date', 'hour', 'airports', 'planes']

    def validate(self, data):
        """
        Check that start is before finish.
        """
        flight_planes = Flight.objects.filter(planes__id=data['planes'].id)

        if data['to'] == data['airports'].city:
            raise serializers.ValidationError("El vuelo no puede ir hacia el mismo aeropuerto")

        elif len(flight_planes) and flight_planes[len(flight_planes) - 1].to == data['to']:
            raise serializers.ValidationError(
                "Un vuelo solo puede ser generado con un avión cuyo último vuelo haya sido al Aeropuerto")
        return data

    def validate_airports(self, value):
        flights_day = Flight.objects.filter(Q(date=datetime.today().date()) & Q(airports__id=value.id))

        if not len(flights_day) <= 20:
            raise serializers.ValidationError("El aeropuerto solo puede tener maximo 20 vuelos por dia")
        return value

    def validate_planes(self, value):
        flights_day = Flight.objects.filter(Q(date=datetime.today().date()) & Q(planes__id=value.id))

        if not len(flights_day) <= 5:
            raise serializers.ValidationError("El avion solo puede tener maximo 5 vuelos")

        return value


class FlightSerializer(serializers.ModelSerializer):
    airports = AirportSerializer(read_only=True)
    planes = PlaneSerializer(read_only=True)

    class Meta:
        model = Flight
        fields = ['id', 'name', 'to', 'date', 'hour', 'airports', 'planes']
