# Create your models here.
from django.db import models
from django import forms
from django.core.exceptions import ValidationError


class Usuario(models.Model):
    nome = models.CharField(max_length=150)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    data_criacao = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return f"{self.nome} <{self.email}>"


class Aluno(Usuario):
    class Meta:
        verbose_name = "Aluno"
        verbose_name_plural = "Alunos"


class Professor(Usuario):
    class Meta:
        verbose_name = "Professor"
        verbose_name_plural = "Professores"


# models.py
from django.core.exceptions import ValidationError
from django.db import transaction

class Materia(models.Model):
    TIPO_CHOICES = [
        ('pessoal', 'Pessoal'),
        ('institucional', 'Institucional'),
    ]
    
    nome = models.CharField(max_length=120, unique=True)
    data_criacao = models.DateTimeField(auto_now_add=True)
    tipo = models.CharField(
        max_length=15,
        choices=TIPO_CHOICES,
        default='institucional'
    )
    
    class Meta:
        ordering = ["nome"]
    
    professor = models.ForeignKey(
        Professor,
        on_delete=models.CASCADE,
        related_name="materias_institucionais",
        null=True,
        blank=True,
        help_text="Professor responsável (para matérias institucionais)"
    )
    
    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE,
        related_name="materias_pessoais",
        null=True,
        blank=True,
        help_text="Aluno responsável (para matérias pessoais)"
    )

    def clean(self):
        if self.tipo == 'institucional' and not self.professor:
            raise ValidationError('Matéria institucional deve ter um professor responsável.')
        
        if self.tipo == 'pessoal' and not self.aluno:
            raise ValidationError('Matéria pessoal deve ter um aluno responsável.')
        
        if self.professor and self.aluno:
            raise ValidationError('Uma matéria não pode ter tanto professor quanto aluno responsável.')

    @transaction.atomic
    def save(self, *args, **kwargs):
        self.full_clean()  # Executa validações
        super().save(*args, **kwargs)
        
        # Cria registro na tabela correspondente
        if self.tipo == 'institucional':
            MateriaInstitucional.objects.update_or_create(
                nome=self.nome,
                defaults={'criador': self.professor}
            )
        elif self.tipo == 'pessoal':
            MateriaPessoal.objects.update_or_create(
                nome=self.nome,
                defaults={'criador': self.aluno}
            )

    def delete(self, *args, **kwargs):
        # Remove também da tabela correspondente
        if self.tipo == 'institucional':
            MateriaInstitucional.objects.filter(nome=self.nome).delete()
        elif self.tipo == 'pessoal':
            MateriaPessoal.objects.filter(nome=self.nome).delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        tipo_display = dict(self.TIPO_CHOICES).get(self.tipo, self.tipo)
        return f"{self.nome} ({tipo_display})"
    
class MateriaInstitucional(models.Model):
    nome = models.CharField(max_length=120, unique=True)
    criador = models.ForeignKey(
        Professor,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text="Professor responsável (para matérias institucionais)"
    )

    class Meta:
        ordering = ["nome"]

    def __str__(self):
        return f"Institucional: {self.nome}"

class MateriaPessoal(models.Model):
    nome = models.CharField(max_length=120, unique=True)
    criador = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        help_text="Aluno responsável ( para matérias pessoais)"
    )

    def __str__(self):
        return f"Pessoal: {self.nome}"

class Questao(models.Model):
    data_criacao = models.DateTimeField(auto_now_add=True)

    materia = models.ForeignKey(
        Materia,
        on_delete=models.CASCADE,
        related_name="questoes",
    )

    professor = models.ForeignKey(
        Professor,
        on_delete=models.CASCADE,
        related_name="questoes_criadas",
    )

    def __str__(self):
        return f"Questão #{self.id} ({self.materia.nome})"


class Alternativa(models.Model):
    texto = models.CharField(max_length=255)
    eh_correta = models.BooleanField(default=False)

    questao = models.ForeignKey(
        Questao,
        on_delete=models.CASCADE,
        related_name="alternativas",
    )

    def __str__(self):
        return f"Alt #{self.id} (Q{self.questao_id})"


class Flashcard(models.Model):
    titulo = models.CharField(max_length=120)
    pergunta = models.TextField()
    resposta = models.TextField()

    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE,
        related_name="flashcards",
    )

    materia = models.ForeignKey(
        Materia,
        on_delete=models.CASCADE,
        related_name="flashcards",
    )

    def __str__(self):
        return self.titulo


class RespostaAluno(models.Model):
    esta_correta = models.BooleanField(default=False)
    data_resposta = models.DateTimeField(auto_now_add=True)

    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE,
        related_name="respostas",
    )

    questao = models.ForeignKey(
        Questao,
        on_delete=models.CASCADE,
        related_name="respostas",
    )

    alternativa_marcada = models.ForeignKey(
        Alternativa,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="respostas_marcadas",
    )

    def __str__(self):
        return f"Resposta #{self.id} (Aluno {self.aluno_id} -> Q{self.questao_id})"