from rest_framework.routers import DefaultRouter, SimpleRouter
from doctors.views import DoctorViewSet


router = SimpleRouter()
router.register('doctors', DoctorViewSet)

urlpatterns = []
urlpatterns += router.urls
