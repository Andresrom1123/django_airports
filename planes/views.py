from datetime import datetime

from django.db.models import Q
from django.shortcuts import get_object_or_404
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
        Devuelve los vuelos del dia de un avión en específico
        """
        plane = get_object_or_404(Plane, Q(flights__date=datetime.today().date()) & Q(id=pk))
        flights = plane.flights.all()
        serialized = FlightSerializer(flights, many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)
