from rest_framework import serializers
from apps.course.models import Curso


class CursoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Curso
        fields = '__all__'
        
        
