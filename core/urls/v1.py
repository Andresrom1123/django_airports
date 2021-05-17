from django.urls import path, include
from rest_framework import routers

from airports.views import AirportViewSet
from flights.views import FlightViewSet
from planes.views import PlaneViewSet

router = routers.DefaultRouter()
router.register(r'airports', AirportViewSet)
router.register(r'planes', PlaneViewSet)
router.register(r'flight', FlightViewSet)

urlpatterns = [
    path('', include(router.urls)),
]