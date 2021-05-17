from rest_framework import viewsets

from flights.models import Flight
from flights.serializers import FlightSerializer


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
