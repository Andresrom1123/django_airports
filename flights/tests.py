from rest_framework.test import APITestCase

from airports.models import Airport
from flights.models import Flight
from planes.models import Plane


class TestFlightViewSet(APITestCase):
    def setUp(self) -> None:
        self.url_base = 'http://127.0.0.1:8000/api/v1/'
        self.plane = Plane.objects.create(name='Avion 1')
        self.airport = Airport.objects.create(name='Aeropuerto 1', city='GDL')
        self.airport.planes.add(self.plane)
        self.flight = Flight.objects.create(name='Vuelo', to='MTY', hour='06:00:00', date='2021-05-18',
                                            airports=self.airport, planes=self.plane)

    def test_action_create_flight(self):
        url = f'{self.url_base}flight/'
        data = {
            'name': 'Vuelo 1',
            'to': 'MTY',
            'hour': '06:00:00',
            'date': '2021-05-18',
            'airports': self.airport.id,
            'planes': self.plane.id
        }
        response = self.client.post(url, data=data)
        print(response.data)
        self.assertEqual(response.status_code, 201)
