from django.urls import path

from cards.views import CardViewSet
from rest_framework import routers

router = routers.SimpleRouter()
router.register('cards', CardViewSet)

urlpatterns = []
urlpatterns += router.urls
