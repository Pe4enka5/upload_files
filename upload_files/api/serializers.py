from rest_framework import serializers 
 
from loader.models import Files 
 
class FilesSerializer(serializers.ModelSerializer): 
    """Сериализатор для файлов""" 
    class Meta: 
        model = Files 
        read_only_fields = ('id', 'processed')
        fields = ('id', 'file', 'uploaded_at', 'processed') 

    def create(self, validated_data):
        file = Files.objects.create(**validated_data)
        file.processed = False
        file.save()
        return file