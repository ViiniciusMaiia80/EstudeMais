from rest_framework import viewsets
from api.aluno import serializers
from api import models

class AlunoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AlunoSerializer
    queryset = models.Aluno.objects.all()