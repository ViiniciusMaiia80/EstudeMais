from rest_framework import serializers
from api import models

class MateriaInstitucionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MateriaInstitucional
        fields = '__all__'