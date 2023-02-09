from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import RetrieveAPIView
from rest_framework import status

from users.models import User
from users.serializers import UserSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserMeAPIView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get(self, request):
        if not request.user.is_authenticated:
            return Response(data='Not authenticated', status=status.HTTP_401_UNAUTHORIZED)

        user = self.get_serializer(request.user).data
        return Response(data=user)
