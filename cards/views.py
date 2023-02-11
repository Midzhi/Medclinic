from rest_framework import viewsets
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.viewsets import ModelViewSet

from cards.models import Card
from cards.serializers import CardSerializer
from cards.permissions import IsOwnerOrCreate


class CardViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = [IsOwnerOrCreate]

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
