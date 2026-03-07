from rest_framework import viewsets
from api.flashcard import serializers
from api import models

class FlashcardViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.FlashcardSerializer
    queryset = models.Flashcard.objects.all()