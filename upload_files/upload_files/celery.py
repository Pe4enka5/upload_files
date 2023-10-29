import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'upload_files.settings')

app = Celery('upload_files')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()