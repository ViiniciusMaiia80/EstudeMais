from rest_framework.test import APITestCase
from api import models


class QuestaoTests(APITestCase):

    def setUp(self):

        #cria professor (post)
        self.professor = models.Professor.objects.create(
            nome="Professor Teste",
            email="prof@test.com",
            senha="123"
        )

        #cria matéria (post)
        self.materia = models.Materia.objects.create(
            nome="Matemática",
            criador=self.professor
        )

    def test_criar_listar_deletar_questao(self):

        #cria questao (post)
        response = self.client.post('/questao/', {
            "materia": self.materia.id,
            "professor": self.professor.id
        })

        self.assertEqual(response.status_code, 201)

        #lista questao (get)
        response = self.client.get('/questao/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.data) > 0)

        questao_id = response.data[0]['id']

        #cria alternativa (post)
        self.client.post('/alternativa/', {
            "texto": "Resposta A",
            "eh_correta": False,
            "questao": questao_id
        })

        self.client.post('/alternativa/', {
            "texto": "Resposta B",
            "eh_correta": True,
            "questao": questao_id
        })

        #verifica se alternativas foram criadas
        alternativas = models.Alternativa.objects.filter(questao_id=questao_id)
        self.assertTrue(alternativas.count() == 2)

        #deleta questao (delete)
        response = self.client.delete(f'/questao/{questao_id}/')
        self.assertEqual(response.status_code, 204)