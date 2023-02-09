from django.urls import path
from mainapp.views import CityViewSet, SpecialityViewSet
from rest_framework import routers

from mainapp.views import PatientViewSet

router = routers.SimpleRouter()
router.register('cities', CityViewSet)
router.register('specialities', SpecialityViewSet)
router.register('patient', PatientViewSet)

urlpatterns = []
urlpatterns += router.urls
