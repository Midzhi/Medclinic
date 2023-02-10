from rest_framework import viewsets
from mainapp.filters import CityFilter, SpecialityFilter
from mainapp.models import City, Speciality
from mainapp.serializers import CitySerializer, SpecialitySerializer
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
