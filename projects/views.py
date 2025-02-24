import requests
from rest_framework.response import Response
from django.http import JsonResponse
from django.shortcuts import render
from .models import Project, Service, RochaProductos
from .serializers import ProjectSerializer, ServiceSerializer, ProductosSerializer
