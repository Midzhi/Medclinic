from rest_framework import viewsets
from rest_framework.parsers import FormParser, MultiPartParser

from mainapp.filters import ArticleFilter
from mainapp.models import Article, ArticleImage
from mainapp.serializers import ArticleSerializer, ArticleImageSerializer
from rest_framework import permissions
from mainapp.permissions import IsOwnerOrAdminReadOnly
from django_filters.rest_framework import DjangoFilterBackend


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrAdminReadOnly
    ]
    filter_backend = [DjangoFilterBackend]
    filterset_class = ArticleFilter

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
