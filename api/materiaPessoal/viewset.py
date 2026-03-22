from rest_framework import viewsets
from api.materiaPessoal import serializers
from api import models

class MateriaPessoalViewSet(viewsets.ModelViewSet):
    serializer_class=serializers.MateriaPessoalSerializer
    queryset = models.MateriaPessoal.objects.all()