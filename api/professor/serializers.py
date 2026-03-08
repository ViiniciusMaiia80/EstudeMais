from api.usuario.serializers import UsuarioSerializer
from api import models

class ProfessorSerializer(UsuarioSerializer):
    class Meta(UsuarioSerializer.Meta):
        model = models.Professor