from rest_framework import viewsets
from api.professor import serializers
from api import models

class ProfessorViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.ProfessorSerializer
    queryset = models.Professor.objects.all()