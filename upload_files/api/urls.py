from django.conf import settings 
from django.conf.urls.static import static 
from django.urls import include, path 
from rest_framework.routers import DefaultRouter 

from api.views import FileListViewSet, FileUploadViewSet

router = DefaultRouter() 
router.register('upload', FileUploadViewSet, basename='file-upload') 
router.register('files', FileListViewSet, basename='file-list') 

urlpatterns = [
    path('', include(router.urls)),
]
