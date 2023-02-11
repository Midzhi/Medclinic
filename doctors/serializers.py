from rest_framework import serializers
from doctors.models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    speciality_name = serializers.ReadOnlyField(source='speciality.name')
    city_name = serializers.ReadOnlyField(source='city.name')

    class Meta:
        model = Doctor
        fields = (
            'id',
            'speciality',
            'speciality_name',
            'city',
            'city_name',
            'working_place',
            'propic',
        )


class DoctorSecondSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField(source='user.full_name')
    speciality_name = serializers.ReadOnlyField(source='speciality.name')
    city_name = serializers.ReadOnlyField(source='city.name')
    email = serializers.ReadOnlyField(source='user.email')

    class Meta:
        model = Doctor
        fields = (
            'id',
            'user',
            'email',
            'full_name',
            'speciality',
            'speciality_name',
            'city',
            'city_name',
            'working_place',
            'propic',
        )
        read_only_fields = ('user',)


class CardDoctorSerialier(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = (
            'id',
            'full_name'
        )