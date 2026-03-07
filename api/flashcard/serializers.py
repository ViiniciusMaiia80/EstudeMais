from rest_framework import serializers
from api import models

class FlashcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Flashcard
        fields = '__all__'