from rest_framework import viewsets
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer

class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo nossos alunos"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    
class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo nossos cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

        
class MatriculaViewSet(viewsets.ModelViewSet):
    """Exibindo nossos cursos"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer