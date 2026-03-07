from rest_framework import serializers
from api import models

class QuestaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Questao
        fields = '__all__'