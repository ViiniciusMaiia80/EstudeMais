from rest_framework import viewsets
from api.respostaAluno import serializers
from api import models

class RespostaAlunoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RespostaAlunoSerializer
    queryset = models.RespostaAluno.objects.all()