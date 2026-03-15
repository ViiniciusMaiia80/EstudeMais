from rest_framework.test import APITestCase
from api import models


class FlashcardTests(APITestCase):

    def setUp(self):

        #cria aluno (post)
        self.aluno = models.Aluno.objects.create(
            nome="Aluno Teste",
            email="aluno@test.com",
            senha="123"
        )

        #cria professor (post)
        self.professor = models.Professor.objects.create(
            nome="Professor Teste",
            email="prof@test.com",
            senha="123"
        )

        #cria matéria (post)
        self.materia = models.Materia.objects.create(
            nome="Biologia",
            criador=self.professor
        )

    def test_criar_listar_deletar_flashcard(self):

        #cria flashcard (post)
        response = self.client.post('/flashcard/', {
            "titulo": "Célula",
            "pergunta": "O que é uma célula?",
            "resposta": "Unidade básica da vida",
            "aluno": self.aluno.id,
            "materia": self.materia.id
        })

        self.assertEqual(response.status_code, 201)

        #listar flashcards (get)
        response = self.client.get('/flashcard/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.data) > 0)

        flashcard_id = response.data[0]['id']

        #deletar flashcard (delete)
        response = self.client.delete(f'/flashcard/{flashcard_id}/')
        self.assertEqual(response.status_code, 204)