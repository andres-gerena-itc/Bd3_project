from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=200)
    created_ad = models.DateTimeField (auto_now_add=True) # Fecha de creación automática

class Service(models.Model):
    country = models.CharField(max_length=100)  # País
    city = models.CharField(max_length=100)  # Ciudad
    seller = models.CharField(max_length=100)  # Vendedor
    service = models.CharField(max_length=200)  # Servicio
    created_at = models.DateTimeField(auto_now_add=True)  # Fecha de creación automática

    def __str__(self):
        return f"{self.service} - {self.city}, {self.country}"