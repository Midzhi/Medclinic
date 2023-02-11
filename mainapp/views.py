from django.utils.decorators import method_decorator
from drf_yasg.utils import swagger_auto_schema
from rest_framework import viewsets
from mainapp.filters import CityFilter, SpecialityFilter
from mainapp.models import City, Speciality
from mainapp.serializers import CitySerializer, SpecialitySerializer
from django_filters.rest_framework import DjangoFilterBackend

@method_decorator(name='list', decorator=swagger_auto_schema(tags=['cities']))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(tags=['cities']))
@method_decorator(name='create', decorator=swagger_auto_schema(tags=['cities']))
@method_decorator(name='update', decorator=swagger_auto_schema(tags=['cities']))
@method_decorator(name='destroy', decorator=swagger_auto_schema(tags=['cities']))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(tags=['cities']))
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


@method_decorator(name='list', decorator=swagger_auto_schema(tags=['specialities']))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(tags=['specialities']))
@method_decorator(name='create', decorator=swagger_auto_schema(tags=['specialities']))
@method_decorator(name='update', decorator=swagger_auto_schema(tags=['specialities']))
@method_decorator(name='destroy', decorator=swagger_auto_schema(tags=['specialities']))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(tags=['specialities']))
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
