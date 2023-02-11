from django.utils.decorators import method_decorator

from rest_framework import viewsets

from drf_yasg.utils import swagger_auto_schema

from appointment.models import Appointment
from appointment.serializers import AppointmentSerializer


@method_decorator(name='list', decorator=swagger_auto_schema(tags=['appointment']))
@method_decorator(name='retrieve', decorator=swagger_auto_schema(tags=['appointment']))
@method_decorator(name='create', decorator=swagger_auto_schema(tags=['appointment']))
@method_decorator(name='update', decorator=swagger_auto_schema(tags=['appointment']))
@method_decorator(name='destroy', decorator=swagger_auto_schema(tags=['appointment']))
@method_decorator(name='partial_update', decorator=swagger_auto_schema(tags=['appointment']))
class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
