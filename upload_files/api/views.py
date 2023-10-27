from rest_framework import viewsets, status
from rest_framework.response import Response

from loader.models import Files
from .serializers import FilesSerializer


class FileUploadViewSet(viewsets.ModelViewSet):
    """ВЬюсет для работы с добавлением файла"""
    queryset = Files.objects.all()
    serializer_class = FilesSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class FileListViewSet(viewsets.ReadOnlyModelViewSet):
    """ВЬюсет для работы отображения всех файлов"""
    queryset = Files.objects.all()
    serializer_class = FilesSerializer
