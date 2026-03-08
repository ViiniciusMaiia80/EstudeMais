from api.usuario.serializers import UsuarioSerializer
from api import models

class AlunoSerializer(UsuarioSerializer):
    class Meta(UsuarioSerializer.Meta):
        model = models.Aluno