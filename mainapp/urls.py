from django.urls import path
from mainapp.views import CityViewSet, SpecialityViewSet
from rest_framework import routers

router = routers.SimpleRouter()
# router.register('appointment', CityViewSet, basename='City')
router.register('appointment', SpecialityViewSet, basename='Speciality')

urlpatterns = []
urlpatterns += router.urls
