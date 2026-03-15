from rest_framework.test import APITestCase
from api import models


class TestMateria(APITestCase):

    def setUp(self):
        #cria um professor
        self.professor = models.Professor.objects.create(
            nome="Professor Teste"
        )

    def test_criar_listar_deletar_materia(self):

        #post (criar materia)
        response = self.client.post('/materia/', {
            "nome": "Matemática",
            "criador": self.professor.id
        })

        self.assertEqual(response.status_code, 201)

        #get (listar materias)
        response = self.client.get('/materia/')

        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.data) > 0)

        #localizar o id da materia criada
        materia_id = response.data[0]['id']

        #delete (deleta a materia criada)
        response = self.client.delete(f'/materia/{materia_id}/')

        self.assertEqual(response.status_code, 204)