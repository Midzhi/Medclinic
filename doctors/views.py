from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.generics import (
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

from doctors.filters import DoctorFilter
from doctors.models import Doctor
from doctors.serializers import DoctorSerializer, DoctorSecondSerializer


class DoctorListAPIView(ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

    filter_backend = [DjangoFilterBackend]
    filterset_class = DoctorFilter


class DoctorDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSecondSerializer
    parser_classes = [MultiPartParser, FormParser]

