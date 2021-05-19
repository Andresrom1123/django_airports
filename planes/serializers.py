from rest_framework import serializers

from planes.models import Plane


class PlaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plane
        fields = ['id', 'name']
