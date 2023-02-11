from rest_framework.routers import DefaultRouter, SimpleRouter

from appointment.views import AppointmentViewSet

router = SimpleRouter()
router.register('appointment', AppointmentViewSet, basename='appointment')

urlpatterns = []
urlpatterns += router.urls
