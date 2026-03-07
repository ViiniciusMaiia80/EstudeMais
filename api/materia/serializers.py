from rest_framework import serializers
from api import models

class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Materia
        fields = '__all__'