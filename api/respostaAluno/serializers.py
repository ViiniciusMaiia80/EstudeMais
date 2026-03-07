from rest_framework import serializers
from api import models

class RespostaAlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Flashcard
        fields = '__all__'