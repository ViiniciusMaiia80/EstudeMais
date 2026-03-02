from rest_framework import serializers
from api import models

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Usuario
        fields = '__all__'
        extra_kwargs = {
            'senha': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }