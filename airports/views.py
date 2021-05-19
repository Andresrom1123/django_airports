from datetime import datetime

from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from airports.models import Airport
from airports.serializers import AirportSerializer, AirportCreateSerializer
from flights.models import Flight
from flights.serializers import FlightSerializer
from planes.serializers import PlaneSerializer


class AirportViewSet(viewsets.ModelViewSet):
    """
    retrieve:
       Regresa un aeropueto con el id.
    list:
        Regresa la lista de aeropuertos.
    create:
        Crea un nuevo aeropuerto.
    delete:
        Borra un aeropuerto.
    update:
        Actualiza un aeropuerto.
    """
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return AirportCreateSerializer
        else:
            return AirportSerializer

    @action(detail=True, methods=['GET'])
    def flights(self, request, pk=None):
        """
        Devuelve los vuelos de un dia de un aeropuerto
        """
        flights = Flight.objects.filter(Q(airports__id=pk) & Q(date=datetime.today().date()))
        serialized = FlightSerializer(flights, many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)

    @action(detail=True, methods=['GET'])
    def planes(self, request, pk=None):
        """
        Devuelve los aviones de un aeropuerto en específico
        """
        airport = get_object_or_404(Airport, id=pk)
        planes = airport.planes.all()
        serialized = PlaneSerializer(planes, many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)
