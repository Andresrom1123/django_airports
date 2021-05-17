from rest_framework import viewsets

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
