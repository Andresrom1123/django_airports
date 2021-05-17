from datetime import datetime

from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from airports.models import Airport
from airports.serializers import AirportSerializer, AirportCreateSerializer
from flights.models import Flight
from flights.serializers import FlightSerializer
from planes.models import Plane


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

    @action(detail=True, methods=['GET', 'POST'])
    def flights(self, request, pk=None):
        airport = Airport.objects.get(id=pk)

        if request.method == 'POST':
            if (id_plane:= request.data.get("id_plane")) and (id_flight:= request.data.get("id_flight")):
                airport_day = Airport.objects.filter(Q(flights__date=datetime.today().date()) & Q(id=pk))
                plane = Plane.objects.get(id=id_plane)
                flight = Flight.objects.get(id=id_flight)

                if len(airport_day.all()) <= 20:
                    if len(plane.flights.all()) <= 5:
                        airport.flights.add(flight)
                        plane.flights.add(flight)

                        airport.save()
                        plane.save()

                        return Response(status=status.HTTP_200_OK)
                    else:
                        Response(status=status.HTTP_400_BAD_REQUEST,
                                 data={'Error': 'El avion solo puede tener maximo 5 vuelos'})
                else:
                    return Response(status=status.HTTP_400_BAD_REQUEST,
                                    data={'Error', 'El aero puerto solo puede tener 20 vuelos por dia'})
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data={'id_plane': 'Es requerido', 'id_flights': 'Es requerido'})
        else:
            flights = airport.flights.all()
            serialized = FlightSerializer(flights, many=True)
            return Response(status=status.HTTP_200_OK, data=serialized.data)
