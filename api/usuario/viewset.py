from api import models
from api.usuario import serializers
from rest_framework import viewsets, status
from api.usuario.serializers import UsuarioSerializer
from api.usuarioCadastro.serializer import CadastrarUsuarioSerializer
from rest_framework.response import Response

class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.UsuarioSerializer
    queryset = models.Usuario.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return CadastrarUsuarioSerializer
        return UsuarioSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = CadastrarUsuarioSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        usuario = serializer.save()

        response_serializer = UsuarioSerializer(usuario)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED)