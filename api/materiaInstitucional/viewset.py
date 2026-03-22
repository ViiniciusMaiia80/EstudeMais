from rest_framework import viewsets
from api.materiaInstitucional import serializers
from api import models

class MateriaInstitucionalViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MateriaInstitucionalSerializer
    queryset = models.MateriaInstitucional.objects.all()