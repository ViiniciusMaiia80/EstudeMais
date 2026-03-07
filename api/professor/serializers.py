from rest_framework import serializers
from api import models

class ProfessorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Professor
        fields = '__all__'