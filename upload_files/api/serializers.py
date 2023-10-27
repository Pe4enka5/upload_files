from rest_framework import serializers 
 
from loader.models import Files 
 
 
class FilesSerializer(serializers.ModelSerializer): 
    """Сериализатор для файлов""" 
    class Meta: 
        model = Files 
        fields = ('id', 'file', 'uploaded_at', 'processed') 
