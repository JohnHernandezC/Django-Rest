from django.db import models

class Inmueble (models.Model):
    direccion=models.CharField(max_length=255)
    pais=models.CharField(max_length=55)
    descripcion=models.CharField(max_length=500)
    imagen=models.CharField(max_length=900)
    active=models.BooleanField(default=True)
    
    def __str__(self):
        return self.direccion
