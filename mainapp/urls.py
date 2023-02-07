from django.urls import path
from doctors.views import DoctorViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('articles', DoctorViewSet)

urlpatterns = []
urlpatterns += router.urls
