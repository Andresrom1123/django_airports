from rest_framework.test import APITestCase

from airports.models import Airport
from flights.models import Flight
from planes.models import Plane


class TestAirportViewSet(APITestCase):
    def setUp(self) -> None:
        self.url_base = 'http://127.0.0.1:8000/api/v1/'
        self.plane = Plane.objects.create(name='Avion 1')
        self.airport = Airport.objects.create(name='Aeropuerto 1', city='GDL')
        self.airport.planes.add(self.plane)
        self.flight = Flight.objects.create(name='Vuelo', to='MTY', hour='06:00:00', date='2021-05-16')

    def test_action_flights(self):
        url = f'{self.url_base}airports/{self.airport.id}/flights/'
        data = {
            'id_plane': self.plane.id,
            'id_flight': self.flight.id
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)
