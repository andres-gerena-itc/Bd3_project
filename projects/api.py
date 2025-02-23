from rest_framework import viewsets, permissions
from .models import Service, Project
from .serializers import ProjectSerializer, ServiceSerializer

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    permission_classes = [permissions.AllowAny]
    serializer_class = ProjectSerializer

class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    permission_classes = [permissions.AllowAny]  # Permitir acceso a todos
    serializer_class = ServiceSerializer