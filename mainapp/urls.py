from mainapp.views import CityViewSet, SpecialityViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('cities', CityViewSet)
router.register('specialities', SpecialityViewSet)

urlpatterns = []
urlpatterns += router.urls
