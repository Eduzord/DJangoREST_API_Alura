
from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewSet, CursosViewSet, MatriculaViewSet , ListaRelacional, ListaAlunosEmCurso
from rest_framework import routers

router = routers.DefaultRouter()

router.register('alunos',AlunosViewSet,basename='Alunos')
router.register('cursos',CursosViewSet,basename='Cursos')
router.register('matriculas',MatriculaViewSet,basename='Matriculas')

urlpatterns = [
    path('admin/', admin.site.urls),
    #eu quero que quando a página alunos seja chamada, quem responda seja a classe alunos
    path('', include(router.urls)) ,
    path('aluno/<int:pk>/matriculas/', ListaRelacional.as_view() ),
    path('curso/<int:pk>/matriculas/', ListaAlunosEmCurso.as_view())
]
