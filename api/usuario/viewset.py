from rest_framework import viewsets
from api.usuario import serializers
from api import models

class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UsuarioSerializer
    queryset = models.Usuario.objects.all()