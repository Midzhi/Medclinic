from rest_framework import serializers
from mainapp.models import City, Speciality, Patient


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


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = (
            'id',
            'name',
            'phone_number',
            'email',
            'date_created',
            'date_updated',
        )