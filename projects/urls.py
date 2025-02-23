from rest_framework import routers
from .api import ProjectViewSet, ServiceViewSet

router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'projects')
router.register('api/services', ServiceViewSet, 'services')

urlpatterns = router.urls