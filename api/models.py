from django.db import models

# Create your models here.
from django.db import models


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


class Materia(models.Model):
    nome = models.CharField(max_length=120)
    data_criacao = models.DateTimeField(auto_now_add=True)

    criador = models.ForeignKey(
        Professor,
        on_delete=models.CASCADE,
        related_name="materias_criadas",
    )

    class Meta:
        unique_together = ("criador", "nome")
        ordering = ["nome"]

    def __str__(self):
        return self.nome


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