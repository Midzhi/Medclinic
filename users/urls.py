from rest_framework.routers import DefaultRouter, SimpleRouter
from users.views import UserViewSet

router = SimpleRouter()
router.register('users', UserViewSet)

urlpatterns = []
urlpatterns += router.urls