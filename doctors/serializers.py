from rest_framework import serializers
from doctors.models import Doctor
from users.models import User


class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = [Doctor, User]
        fields = (
            'id',
            'user',
            'speciality',
            'working_place',
            'propic',

        )

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data.get('password'))
        user.save()
        return user

