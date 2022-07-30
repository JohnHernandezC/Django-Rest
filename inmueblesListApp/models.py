from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator
from django.contrib.auth.models import User
class Empresa (models.Model):
    nombre=models.CharField(max_length=250)
    website=models.URLField(max_length=250)
    active=models.BooleanField(default=True)
    def __str__(self):
        return self.nombre
    
class Edificacion (models.Model):
    direccion=models.CharField(max_length=255)
    pais=models.CharField(max_length=55)
    descripcion=models.CharField(max_length=500)
    imagen=models.CharField(max_length=900)
    avg_calificacion=models.FloatField(default=0)
    number_Calificacion=models.FloatField(default=0)
    empresa=models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="EdificacionList")
    active=models.BooleanField(default=True)
    created=models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.direccion
    
class Comentarios (models.Model):
    Comentarios_user=models.ForeignKey(User, on_delete=models.CASCADE)
    calificacion=models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    texto=models.CharField(max_length=250, null=True)
    inmuebles=models.ForeignKey(Edificacion, on_delete=models.CASCADE, related_name="comentarios")
    active=models.BooleanField(default=True)
    created=models.DateField(auto_now_add=True)  
    update=models.DateField(auto_now_add=True) 
    def __str__(self):
        return str(self.calificacion)+" "+self.inmuebles.direccion   

    
