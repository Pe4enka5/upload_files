from celery import shared_task
from .models import Files


@shared_task
def process_file(file_id):
    """Функция для обработки файла"""
    file = Files.objects.get(id=file_id)
    file.processed = True
    file.save()