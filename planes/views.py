from datetime import datetime

from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from flights.models import Flight
from flights.serializers import FlightSerializer
from planes.models import Plane
from planes.serializers import PlaneSerializer


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

    @action(detail=True, methods=['GET'])
    def flights(self, request, pk=None):
        """
        Devuelve los vuelos del dia de un avión en específico
        """
        flights = Flight.objects.filter(Q(planes__id=pk) & Q(date=datetime.today().date()))
        serialized = FlightSerializer(flights, many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)
