from rest_framework import serializers
from . models import Aluno

class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fieds = '__all__'
        