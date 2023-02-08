from rest_framework import serializers
from doctors.models import Doctor


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = (
            'id',
            'user',
            'speciality',
            'working_place',
            'propic',

        )

    def create(self, validated_data):
        doctor = Doctor(**validated_data)
        doctor.set_password(validated_data.get('password'))
        doctor.save()
        return doctor

