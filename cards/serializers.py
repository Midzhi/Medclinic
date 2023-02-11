from rest_framework import serializers
from cards.models import Card
from doctors.serializers import DoctorSerializer, DoctorSecondSerializer

from users.serializers import UserSerializer


class CardSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = Card
        fields = (
            'id',
            'user',
            'schedule',
            'workload',
            'price'
        )
        read_only_fields = ('user',)

    def create(self, validated_data):
        card = Card.objects.create(**validated_data)
        return card


# class CardSerializer(serializers.ModelSerializer):
#     doctor_id = serializers.ReadOnlyField(source='doctor.id')
#     full_name = serializers.ReadOnlyField(source='user.full_name')
#     speciality_name = serializers.ReadOnlyField(source='doctor.speciality')
#     city_name = serializers.ReadOnlyField(source='doctor.city')
#     working_place = serializers.ReadOnlyField(source='doctor.working_place')
#     propic = serializers.ReadOnlyField(source='doctor.propic')
#
#     class Meta:
#         model = Card
#         fields = (
#             'id',
#             'doctor_id'
#             'full_name',
#             'speciality_name',
#             'city_name',
#             'working_place',
#             'propic',
#             'schedule',
#             'workload',
#             'price',
#         )
