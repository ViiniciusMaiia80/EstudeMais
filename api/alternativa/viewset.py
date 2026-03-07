from rest_framework import viewsets
from api.alternativa import serializers
from api import models

class AlternativaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.AlternativaSerializer
    queryset = models.Alternativa.objects.all()