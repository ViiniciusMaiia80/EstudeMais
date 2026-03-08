from rest_framework import viewsets
from api.usuarioCadastro.serializer import UsuarioSerializer, CadastrarUsuarioSerializer
from api import models

class UsuarioViewSet(viewsets.ModelViewSet):
    query = models.Usuario.objects.all()

    def get_serializer_class(self):
        if self.action == 'create':
            return CadastrarUsuarioSerializer
        return UsuarioSerializer