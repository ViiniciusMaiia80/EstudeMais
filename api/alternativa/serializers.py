from rest_framework import serializers
from api import models

class AlternativaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Alternativa
        fields = '__all__'