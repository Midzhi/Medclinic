from rest_framework import serializers
from users.models import User

from doctors.serializers import DoctorSerializer
from doctors.models import Doctor


class UserSerializer(serializers.ModelSerializer):
    doctor = DoctorSerializer()

    class Meta:
        model = User
        fields = (
            'id',
            'email',
            'first_name',
            'last_name',
            'full_name',
            'phone_number',
            'doctor',
            'password'
        )
        read_only_fields = ('full_name',)
        extra_kwargs = {
            'password': {'write_only': True},
            'first_name': {'write_only': True},
            'last_name': {'write_only': True},
        }

    def create(self, validated_data):
        doctor = validated_data.pop('doctor')
        user = User(**validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        Doctor.objects.create(
            user=user,
            city=doctor.get('city'),
            speciality=doctor.get('speciality'),
            working_place=doctor.get('working_place')
        )
        return user
