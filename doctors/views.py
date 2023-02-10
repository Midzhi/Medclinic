from rest_framework.generics import (
    RetrieveAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser, FormParser

from doctors.models import Doctor
from doctors.serializers import DoctorSerializer, DoctorSecondSerializer


class DoctorListAPIView(ListAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSecondSerializer


class DoctorDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSecondSerializer
    parser_classes = [MultiPartParser, FormParser]
