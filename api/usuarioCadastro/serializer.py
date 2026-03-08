from rest_framework import serializers
from django.contrib.auth.hashers import make_password
from api import models

class CadastrarUsuarioSerializer(serializers.Serializer):
    TIPO_CHOICES = (
        ('aluno', 'Aluno'),
        ('professor', 'Professor'),
    )

    nome = serializers.CharField(max_length=150)
    email = serializers.EmailField()
    senha = serializers.CharField(write_only=True, style={'input_type': 'password'})
    tipo_usuario = serializers.ChoiceField(choices=TIPO_CHOICES, write_only=True)

    def validate_nome(self, value):
        value = value.strip().lower()
        if not value:
            raise serializers.ValidationError("O nome é obrigatório!")
        return value
    
    def validate_email(self, value):
        value = value.strip().lower()
        if models.Usuario.objects.filter(email=value).exists():
            raise serializers.ValidationError("Já existe um usuário com esse email.")
        return value
    
    def validate_senha(self, value):
        if not value or not value.strip():
            raise serializers.ValidationError("A senha é obrigatória!")
        if len(value) < 6:
            raise serializers.ValidationError("A senha deve ter no mínimo 6 caracteres.")
        return value
    
    def create(self, validated_data):
        tipo_usuario = validated_data.pop('tipo_usuario')
        validated_data['senha'] = make_password(validated_data['senha'])
        if tipo_usuario == 'aluno':
            return models.Aluno.objects.create(**validated_data)
        return models.Professor.objects.create(**validated_data)