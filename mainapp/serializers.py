from rest_framework import serializers
from mainapp.models import City, Speciality


class CitySerializer(serializers.ModelSerializer):
    city = serializers.ReadOnlyField(source='name')

    class Meta:
        model = City
        fields = (
            'id',
            'name',
        )
        read_only_fields = (
            'name',
        )


class SpecialitySerializer(serializers.ModelSerializer):
    speciality = serializers.ReadOnlyField(source='name')

    class Meta:
        model = Speciality
        fields = (
            'id',
            'name',
        )
        read_only_fields = (
            'name',
        )