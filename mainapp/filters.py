from django_filters import rest_framework as filters

from mainapp.models import City, Speciality


class CityFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = City
        fields = (
            'name',
        )


class SpecialityFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='contains')

    class Meta:
        model = Speciality
        fields = (
            'name',
        )