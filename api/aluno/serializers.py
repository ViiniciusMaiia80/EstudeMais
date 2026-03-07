from rest_framework import serializers
from api import models

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Aluno
        fields = '__all__'