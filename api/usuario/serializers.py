from django.contrib.auth.hashers import make_password
from rest_framework import serializers
from api import models

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Usuario
        fields = ['id', 'nome', 'email', 'senha', 'data_criacao']
        read_only_fields = ['id', 'data_criacao']
        extra_kwargs = {
            'senha': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def validate_email(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("O email é obrigatório!")
        return value

    def create(self, validated_data):
        validated_data['senha'] = make_password(validated_data['senha'])
        return super().create(validated_data)

    def update(self, instance, validated_data):
        if 'senha' in validated_data:
            validated_data['senha'] = make_password(validated_data['senha'])
        return super().update(instance, validated_data)

    def validate_senha(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("A senha é obrigatória!")
        if len(value) < 6:
            raise serializers.ValidationError("A senha deve ter no mínimo 6 caracteres.")
        return value