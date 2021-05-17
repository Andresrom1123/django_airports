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

    @action(detail=True, methods=['GET', 'POST'])
    def flights(self, request, pk=None):
        """
        Devuelve los vuelos de un dia de un aeropuerto en específico y manda un vuelo a un avion y aeropuerto
        """
        airport = Airport.objects.get(id=pk)

        if request.method == 'POST':
            if (id_plane:= request.data.get("id_plane")) and (id_flight:= request.data.get("id_flight")):
                airport_day = Airport.objects.filter(Q(flights__date=datetime.today().date()) & Q(id=pk))
                plane = Plane.objects.get(id=id_plane)
                flight = Flight.objects.get(id=id_flight)

                if airport.city == flight.to:
                    return Response(status=status.HTTP_400_BAD_REQUEST,
                                    data={'Error': 'El vuelo no puede ir hacia el mismo aeropuerto'})
                if len(plane.flights.all()) > 0 \
                        and not plane.flights.all()[len(plane.flights.all()) - 1].to == airport.city:
                    return Response(
                        status=status.HTTP_400_BAD_REQUEST, data={
                            'Error':
                            'Un vuelo solo puede ser generado con un avión cuyo último vuelo haya sido al Aeropuerto'})
                if not len(airport_day.all()) <= 20:
                    return Response(status=status.HTTP_400_BAD_REQUEST,
                                    data={'Error', 'El aero puerto solo puede tener 20 vuelos por dia'})
                if not len(plane.flights.all()) <= 5:
                    return Response(status=status.HTTP_400_BAD_REQUEST,
                                    data={'Error': 'El avion solo puede tener maximo 5 vuelos'})

                airport.flights.add(flight)
                plane.flights.add(flight)

                airport.save()
                plane.save()

                return Response(status=status.HTTP_200_OK)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST,
                                data={'id_plane': 'Es requerido', 'id_flight': 'Es requerido'})
        else:
            airport_day = Airport.objects.filter(Q(flights__date=datetime.today().date()) & Q(id=pk))
            flights = airport_day.all()
            serialized = FlightSerializer(flights, many=True)
            return Response(status=status.HTTP_200_OK, data=serialized.data)

    @action(detail=True, methods=['GET', 'POST'])
    def planes(self, request, pk=None):
        """
        Devuelve los aviones de un aeropuerto en específico
        """
        airport = Airport.objects.get(id=pk)
        planes = airport.planes.all()
        serialized = PlaneSerializer(planes, many=True)
        return Response(status=status.HTTP_200_OK, data=serialized.data)
