from rest_framework import viewsets, status
from rest_framework.response import Response

from airports.models import Airport
from flights.models import Flight
from flights.serializers import FlightSerializer, FlightCreateSerializer
from planes.models import Plane


class FlightViewSet(viewsets.ModelViewSet):
    """
    retrieve:
       Regresa un vuelo con el id.
    list:
        Regresa la lista de vuelos.
    create:
        Crea un nuevo vuelo.
    delete:
        Borra un vuelo.
    update:
        Actualiza un vuelo.
    """
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return FlightCreateSerializer
        else:
            return FlightSerializer
