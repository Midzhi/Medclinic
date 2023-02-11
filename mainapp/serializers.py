from rest_framework import serializers
from mainapp.models import City, Speciality


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = (
            'id',
            'name',
        )


class SpecialitySerializer(serializers.ModelSerializer):

    class Meta:
        model = Speciality
        fields = (
            'id',
            'name'
        )
