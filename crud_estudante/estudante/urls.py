from django.urls import path
from . import views

urlpatterns = [
    path('aluno/', views.listar_alunos),
    path('aluno/criar/', views.criar_aluno),
]