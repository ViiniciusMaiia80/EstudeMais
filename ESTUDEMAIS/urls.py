from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from api.usuario import viewset as usuarioviewset
from api.materia import viewset as materiaviewset
from api.aluno import viewset as alunoviewset
from api.professor import viewset as professorviewset
from api.questao import viewset as questaoviewset
from api.alternativa import viewset as alternativaviewset
from api.flashcard import viewset as flashcardviewset
from api.respostaAluno import viewset as respostaalunoviewset
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

route = routers.DefaultRouter()
route.register(r'usuario', usuarioviewset.UsuarioViewSet, basename="usuario")
route.register(r'materia', materiaviewset.MateriaViewSet, basename="materia")
route.register(r'aluno', alunoviewset.AlunoViewSet, basename="aluno")
route.register(r'professor', professorviewset.ProfessorViewSet, basename="professor")
route.register(r'questao', questaoviewset.QuestaoViewSet, basename="questao")
route.register(r'alternativa', alternativaviewset.AlternativaViewSet, basename="alternativa")
route.register(r'flashcard', flashcardviewset.FlashcardViewSet, basename="flashcard")
route.register(r'resposta-aluno', respostaalunoviewset.RespostaAlunoViewSet, basename="respostaAluno")

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(route.urls)),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path("api/docs/", SpectacularSwaggerView.as_view(url_name="schema"), name="swagger-ui"),
    path("api/", include("api.urls")),
]