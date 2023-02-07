from rest_framework import serializers
from mainapp.models import City, Speciality


class AppointmentSerializer(serializers.ModelSerializer):
    author_name = serializers.ReadOnlyField(source='email.username')

    class Meta:
        model = [City, Speciality]
        fields = (
            'id',
            'name',

        )
        read_only_fields = (
            'name',
        )

