from rest_framework import serializers
from.models import *

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('id', 'title', 'description','technology','created_ad')
        read_only_fields = ('created_ad', )
        
class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = ('id', 'country', 'city', 'seller', 'service', 'created_at')
        read_only_fields = ('created_at', )