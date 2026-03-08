from django.contrib import admin
from .models import (
    Usuario,
    Aluno,
    Professor,
    Materia,
    Questao,
    Alternativa,
    Flashcard,
    RespostaAluno
)

admin.site.register(Usuario)
admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Materia)
admin.site.register(Questao)
admin.site.register(Alternativa)
admin.site.register(Flashcard)
admin.site.register(RespostaAluno)

# Register your models here.
