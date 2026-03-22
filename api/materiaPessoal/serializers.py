from rest_framework import serializers
from api import models

class MateriaPessoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MateriaPessoal
        fields = '__all__'

