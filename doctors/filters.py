from django_filters import rest_framework as filters

from doctors.models import Doctor


class DoctorFilter(filters.FilterSet):
    city = filters.CharFilter(lookup_expr='contains')
    speciality = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Doctor
        fields = (
            'city',
            'speciality',
        )