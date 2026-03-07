from rest_framework import viewsets
from api.materia import serializers
from api import models

class MateriaViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.MateriaSerializer
    queryset = models.Materia.objects.all()