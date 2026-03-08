from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from api import models


class UsuarioSerializer(serializers.ModelSerializer):
    senha = serializers.CharField(
        write_only=True,
        required=False,
        style={'input_type': 'password'}
    )
    tipo_usuario = serializers.SerializerMethodField()

    class Meta:
        model = models.Usuario
        fields = ['id', 'nome', 'email', 'senha', 'tipo_usuario', 'data_criacao']
        read_only_fields = ['id', 'data_criacao', 'tipo_usuario']

    def get_tipo_usuario(self, obj):
        if hasattr(obj, 'aluno'):
            return 'aluno'
        if hasattr(obj, 'professor'):
            return 'professor'
        return 'usuario'

    def update(self, instance, validated_data):
        if 'senha' in validated_data:
            validated_data['senha'] = make_password(validated_data['senha'])
        return super().update(instance, validated_data)