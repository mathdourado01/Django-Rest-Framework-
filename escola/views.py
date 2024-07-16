from rest_framework import viewsets, generics
from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, ListaAlunosMatriculadosSerializer
from rest_framework.authentication import BasicAuthentication   
from rest_framework.permissions import IsAuthenticated
class AlunosViewSet(viewsets.ModelViewSet):
    """Exibindo nossos alunos"""
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer
    authentication_classes = [BasicAuthentication]
    permissions_classes = [IsAuthenticated]
class CursosViewSet(viewsets.ModelViewSet):
    """Exibindo nossos cursos"""
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

        
class MatriculaViewSet(viewsets.ModelViewSet):
    """Exibindo nossos cursos"""
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class ListaMatriculasAluno(generics.ListAPIView):
    """Listando as matriculas do aluno"""
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer    
    
class ListaAlunosMatriculados(generics.ListAPIView):
    '''Listando alunos e alunos matriculados em um curso '''
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id = self.kwargs['pk'])
        return queryset
    serializer_class = ListaAlunosMatriculadosSerializer 
    
    