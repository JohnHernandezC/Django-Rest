
from rest_framework.response import Response
from django.http import JsonResponse
from django.shortcuts import render
from inmueblesListApp.api.serializers import InmuebleSerializer
#from rest_framework.decorators import api_view
from inmueblesListApp.models import Inmueble
from rest_framework import status
from rest_framework.views import APIView


class InmueblesListAv(APIView):
    def get(self, request):
        inmuebles=Inmueble.objects.all()
        serializer=InmuebleSerializer(inmuebles, many=True)
        return Response(serializer.data)
    def post(self, request):
        deserializer=InmuebleSerializer(data=request.data)
        if deserializer.is_valid():
            deserializer.save()
            return Response(deserializer.data)
        else:
             return Response(deserializer.errors, status=status.HTTP_400_BAD_REQUEST)

class InmuebleDetalleAv(APIView):
    def get(self, request,pk):
        try:
            inmueble=Inmueble.objects.get(pk=pk)
        except Inmueble.DoesNotExist:
            return Response(('Error el inmueble no existe'), status=status.HTTP_404_NOT_FOUND)
        serializer=InmuebleSerializer(inmueble)
        return Response(serializer.data)
        
    def put(self, request,pk):
        try:
            inmueble=Inmueble.objects.get(pk=pk)
        except Inmueble.DoesNotExist:
            return Response(('Error el inmueble no existe'), status=status.HTTP_404_NOT_FOUND)
        deserializer=InmuebleSerializer(inmueble, data=request.data)
        if deserializer.is_valid():
            deserializer.save()
            return Response(deserializer.data)
        else:
             return Response(deserializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request,pk):
        try:
            inmueble=Inmueble.objects.get(pk=pk)
        except Inmueble.DoesNotExist:
            return Response(('Error el inmueble no existe'), status=status.HTTP_404_NOT_FOUND)
        inmueble.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        
            


# FUNCIONES TIPO DJANGO PARA CRUD
# @api_view(['GET','POST'])
# def inmuebleList(request):
#     if request.method == 'GET':
#         inmuebles=Inmueble.objects.all()
#         serializer=InmuebleSerializer(inmuebles, many=True)
#         return Response(serializer.data)
#     if request.method == 'POST':
#         deserializer=InmuebleSerializer(data=request.data)
#         if deserializer.is_valid():
#             deserializer.save()
#             return Response(deserializer.data)
#         else:
#             return Response(deserializer.errors)
        

# @api_view(['GET','PUT','DELETE'])
# def inmuebledetalle (request,pk):
#     if request.method == 'GET':
#         try:
#             inmueble=Inmueble.objects.get(pk=pk)
#             serializer=InmuebleSerializer(inmueble)
#             return Response(serializer.data)
#         except Inmueble.DoesNotExist:
#             return Response(('Error el inmueble no existe'), status=status.HTTP_404_NOT_FOUND)
    
#     if request.method == 'PUT':
#         inmueble=Inmueble.objects.get(pk=pk)
#         deserializer=InmuebleSerializer(inmueble, data=request.data)
#         if deserializer.is_valid():
#             deserializer.save()
#             return Response(deserializer.data)
#         else:
#             return Response(deserializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == 'DELETE':
#         try:
#             inmueble=Inmueble.objects.get(pk=pk)
#             inmueble.delete()
#             data={'resultado':True}
#         except Inmueble.DoesNotExist:
#             return Response(('Error el inmueble no existe'), status=status.HTTP_404_NOT_FOUND)
#         return Response(status=status.HTTP_204_NO_CONTENT)