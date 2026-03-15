from rest_framework.test import APITestCase
from api import models


class RespostaAlunoTests(APITestCase):

    def setUp(self):

        #cria professor
        self.professor = models.Professor.objects.create(
            nome="Professor Teste",
            email="prof@test.com",
            senha="123"
        )

        #cria aluno
        self.aluno = models.Aluno.objects.create(
            nome="Aluno Teste",
            email="aluno@test.com",
            senha="123"
        )

        #cria matéria
        self.materia = models.Materia.objects.create(
            nome="História",
            criador=self.professor
        )

        #cria questão
        self.questao = models.Questao.objects.create(
            materia=self.materia,
            professor=self.professor
        )

        #cria alternativas
        self.alt1 = models.Alternativa.objects.create(
            texto="1500",
            eh_correta=True,
            questao=self.questao
        )

        self.alt2 = models.Alternativa.objects.create(
            texto="1800",
            eh_correta=False,
            questao=self.questao
        )

    def test_aluno_responde_questao(self):

        #aluno responde a questão
        response = self.client.post('/resposta-aluno/', {
            "aluno": self.aluno.id,
            "questao": self.questao.id,
            "alternativa_marcada": self.alt1.id,
            "esta_correta": True
        })

        print(response.data)
        self.assertEqual(response.status_code, 201)

        #verificar se foi registrada
        resposta = models.RespostaAluno.objects.first()

        self.assertEqual(resposta.aluno.id, self.aluno.id)
        self.assertEqual(resposta.questao.id, self.questao.id)
        self.assertEqual(resposta.alternativa_marcada.id, self.alt1.id)