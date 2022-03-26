"""from django.http import JsonResponse
from django.shortcuts import render

from .models import Inmueble

# Create your views here.
def inmuebleList (request):
    inmueble=Inmueble.objects.all()
    data={
        'inmueble':list(inmueble.values())
        }
    return JsonResponse(data)

def inmuebledetalle (request,pk):
    inmueble=Inmueble.objects.get(pk=pk)
    data={
        'direccion':inmueble.direccion,
        'pais':inmueble.pais,
        'descripcion':inmueble.descripcion,
        'imagen':inmueble.imagen,
        'active':inmueble.active,
        }
    return JsonResponse(data)"""