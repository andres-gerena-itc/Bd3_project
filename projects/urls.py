from rest_framework import routers
from .api import ProjectViewSet, ServiceViewSet
from django.urls import path
from . import views

router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'projects')
router.register('api/services', ServiceViewSet, 'services')

urlpatterns = router.urls



    
