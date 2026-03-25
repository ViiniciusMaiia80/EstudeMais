from django.db import models

# Create your models here.
from django.db import models


class Usuario(models.Model):
    nome = models.CharField(max_length=150, help_text="Nome completo do usuário.")
    email = models.EmailField(unique=True, help_text="E-mail único do usuário.")
    senha = models.CharField(max_length=128, help_text="Senha cadastrada para acesso ao sistema.")
    data_criacao = models.DateTimeField(auto_now_add=True, help_text="Data de criação do usuário.")

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
    nome = models.CharField(max_length=120, help_text="Nome da matéria.")
    data_criacao = models.DateTimeField(auto_now_add=True, help_text="Data de criação da matéria.")
    criador = models.ForeignKey(
        Professor,
        on_delete=models.CASCADE,
        related_name="materias_criadas",
        help_text="Professor responsável pela criação da matéria."
    )

    class Meta:
        unique_together = ("criador", "nome")
        ordering = ["nome"]

    def __str__(self):
        return self.nome


class Questao(models.Model):
    materia = models.ForeignKey(
        Materia,
        on_delete=models.CASCADE,
        related_name="questoes",
        help_text="Matéria à qual a questão pertence."
    )
    professor = models.ForeignKey(
        Professor,
        on_delete=models.CASCADE,
        related_name="questoes_criadas",
        help_text="Professor responsável pela criação da questão."
    )
    data_criacao = models.DateTimeField(auto_now_add=True, help_text="Data de criação da questão.")
    def __str__(self):
        return f"Questão #{self.id} ({self.materia.nome})"


class Alternativa(models.Model):
    texto = models.CharField(max_length=255, help_text="Texto da alternativa.")
    eh_correta = models.BooleanField(default=False, help_text="Indica se esta alternativa é a correta.")
    questao = models.ForeignKey(
        Questao,
        on_delete=models.CASCADE,
        related_name="alternativas",
        help_text="Questão à qual a alternativa pertence."
    )

    def __str__(self):
        return f"Alt #{self.id} (Q{self.questao_id})"


class Flashcard(models.Model):
    pergunta = models.TextField(help_text="Pergunta principal do flashcard.")
    resposta = models.TextField(help_text="Resposta do flashcard.")
    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE,
        related_name="flashcards",
        help_text="Aluno responsável pela criação do flashcard."
    )
    materia = models.ForeignKey(
        Materia,
        on_delete=models.CASCADE,
        related_name="flashcards",
        help_text="Matéria à qual o flashcard pertence."
    )

    def __str__(self):
        return f"Flashcard {self.id}"


class RespostaAluno(models.Model):
    esta_correta = models.BooleanField(default=False, help_text="Indica se a resposta do aluno está correta.")
    data_resposta = models.DateTimeField(auto_now_add=True, help_text="Data em que a resposta foi enviada.")
    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.CASCADE,
        related_name="respostas",
        help_text="Aluno que respondeu a questão."
    )
    questao = models.ForeignKey(
        Questao,
        on_delete=models.CASCADE,
        related_name="respostas",
        help_text="Questão respondida pelo aluno."
    )
    alternativa_marcada = models.ForeignKey(
        Alternativa,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="respostas_marcadas",
        help_text="Alternativa marcada pelo aluno, quando houver."
    )

    def __str__(self):
        return f"Resposta #{self.id} (Aluno {self.aluno_id} -> Q{self.questao_id})"