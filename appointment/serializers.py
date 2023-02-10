from rest_framework import serializers
from appointment.models import Appointment


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = (
            'id',
            'doctor',
            'name',
            'phone_number',
            'email',
            'date_created',
            'date_updated',
        )
