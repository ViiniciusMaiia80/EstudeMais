from rest_framework import serializers
from api import models

class RespostaAlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RespostaAluno
        fields = '__all__'