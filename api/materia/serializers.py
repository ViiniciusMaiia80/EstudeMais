# serializers.py
from rest_framework import serializers
from api import models

class MateriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Materia
        fields = '__all__'

    def validate(self, data):
        tipo = data.get('tipo')
        professor = data.get('professor')
        aluno = data.get('aluno')

        if tipo == 'institucional' and not professor:
            raise serializers.ValidationError(
                {'professor': 'Matéria institucional deve ter um professor responsável.'}
            )
        
        if tipo == 'pessoal' and not aluno:
            raise serializers.ValidationError(
                {'aluno': 'Matéria pessoal deve ter um aluno responsável.'}
            )
        
        if professor and aluno:
            raise serializers.ValidationError(
                {'non_field_errors': 'Uma matéria não pode ter tanto professor quanto aluno responsável.'}
            )

        return data
    
    # serializers.py - Adicione estes serializers
class MateriaInstitucionalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MateriaInstitucional
        fields = '__all__'

class MateriaPessoalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.MateriaPessoal
        fields = '__all__'