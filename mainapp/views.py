from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser

from doctors.models import Doctor
from doctors.serializers import DoctorSerializer
from mainapp.filters import CityFilter, SpecialityFilter
from mainapp.models import City, Speciality
from mainapp.serializers import CitySerializer, SpecialitySerializer
from rest_framework import permissions
from mainapp.permissions import IsOwnerOrAdminReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class CityViewSet(viewsets.ModelViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    # permission_classes = [
    #     permissions.IsAuthenticatedOrReadOnly,
    #     IsOwnerOrAdminReadOnly
    # ]
    filter_backend = [DjangoFilterBackend]
    filterset_class = CityFilter

    def perform_create(self, serializer):
        serializer.save(name=self.request.name)

class SpecialityViewSet(viewsets.ModelViewSet):
    queryset = Speciality.objects.all()
    serializer_class = SpecialitySerializer
    # permission_classes = [
    #     permissions.IsAuthenticatedOrReadOnly,
    #     IsOwnerOrAdminReadOnly
    # ]
    filter_backend = [DjangoFilterBackend]
    filterset_class = SpecialityFilter

    def perform_create(self, serializer):
        serializer.save(name=self.request.name)

