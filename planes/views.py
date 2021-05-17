from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from flights.serializers import FlightSerializer
from planes.models import Plane
from planes.serializers import PlaneSerializer, PlaneCreateSerializer


class PlaneViewSet(viewsets.ModelViewSet):
    """
    retrieve:
       Regresa un avion con el id.
    list:
        Regresa la lista de aviones.
    create:
        Crea un nuevo avion.
    delete:
        Borra un avion.
    update:
        Actualiza un avion.
    """
    queryset = Plane.objects.all()
    serializer_class = PlaneSerializer

    def get_serializer_class(self):
        if self.action == 'create':
            return PlaneCreateSerializer
        else:
            return PlaneSerializer

    @action(detail=True, methods=['GET'])
    def flights(self, request, pk=None):
        """
        Devuelve los vuelos de un avión en específico
        """
        plane = Plane.objects.get(id=pk)
        flights = plane.flights.all()
        serialized = FlightSerializer(flights, many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)
