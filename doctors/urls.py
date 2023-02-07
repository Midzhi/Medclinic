from rest_framework.routers import DefaultRouter, SimpleRouter
from users.views import UserViewSet


router = SimpleRouter()
router.register('doctors', UserViewSet)

urlpatterns = []
urlpatterns += router.urls