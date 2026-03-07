from rest_framework import viewsets
from api.questao import serializers
from api import models

class QuestaoViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.QuestaoSerializer
    queryset = models.Questao.objects.all()