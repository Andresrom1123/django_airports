from rest_framework.test import APITestCase

from airports.models import Airport
from flights.models import Flight
from planes.models import Plane


class TestAirportViewSet(APITestCase):
    def setUp(self) -> None:
        self.url_base = 'http://127.0.0.1:8000/api/v1/'
        self.plane = Plane.objects.create(name='Avion 1')
        self.plane_2 = Plane.objects.create(name='Avion 2')
        self.airport = Airport.objects.create(name='Aeropuerto 1', city='GDL')
        self.airport.planes.add(self.plane)
        self.flight = Flight.objects.create(name='Vuelo', to='MTY', hour='06:00:00', date='2021-05-17')
        self.airport_2 = Airport.objects.create(name='Aeropuerto 2', city='MTY')
        self.airport_2.flights.add(self.flight)

    def test_action_post_flights(self):
        url = f'{self.url_base}airports/{self.airport.id}/flights/'
        data = {
            'id_plane': self.plane.id,
            'id_flight': self.flight.id
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, 200)
        self.airport.refresh_from_db()
        flight_2 = Flight.objects.create(name='Vuelo 2', to='CDMX', hour='06:00:00', date='2021-05-17')
        data_2 = {
            'id_plane': self.plane_2.id,
            'id_flight': flight_2.id
        }
        response_2 = self.client.post(url, data=data_2)
        self.assertEqual(response_2.status_code, 200)

    def test_action_get_flights(self):
        url = f'{self.url_base}airports/{self.airport_2.id}/flights/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_action_planes(self):
        url = f'{self.url_base}airports/{self.airport.id}/planes/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
