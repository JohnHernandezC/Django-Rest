
from inmueblesListApp.api.permissions import adminOrReadOnly,ComentarioUserOrReadOnly
from rest_framework.response import Response
from django.http import JsonResponse
from django.shortcuts import render
from inmueblesListApp.api.serializers import EdificacionSerializer,EmpresaSerializer,ComentarioSerializer
#from rest_framework.decorators import api_view
from inmueblesListApp.models import Edificacion, Empresa, Comentarios
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics , mixins
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated


#la clase comentario la trabajamos de manera generica con metodos get y post genericos
#metodo 1
class ComentarioCreate (generics.CreateAPIView ):
    serializer_class = ComentarioSerializer
    
    def get_queryset(self):
        return Comentarios.objects.all()
    def perform_create(self, serializer):
        
        pk=self.kwargs['pk']#me entrega todas las propiedades que me da el cliente  de ahi puedo sacar todo
        edificacion=Edificacion.objects.get(pk=pk)
        user=self.request.user
        #hacemos un a comprobacion de si el usuario ya a registrado un comentario con anterioridad
        comentario_queryset=Comentarios.objects.filter(inmuebles=edificacion,Comentarios_user=user)#este inmuebles hace referencia al de la base de datos
        if comentario_queryset.exists():
            raise ValidationError('El usuario ya escribio un comentario para este inmueble')
        #/Modificar  los comentarios (cantidad y promediio)
        if edificacion.number_Calificacion==0:
            edificacion.avg_calificacion=serializer.validated_data['calificacion']
        else:
            edificacion.avg_calificacion=(serializer.validated_data['calificacion']+edificacion.avg_calificacion)/2 #esto es para saber el promedio
        edificacion.number_Calificacion+=1
        edificacion.save()
                
        serializer.save(inmuebles=edificacion, Comentarios_user=user)
        
        
    
class ComentarioLis(generics.ListCreateAPIView ):
    permission_classes = [IsAuthenticated]
    #queryset = Comentarios. objects. all()
    serializer_class = ComentarioSerializer
    #-////////mostrar todos
    def get_queryset(self):
        pk=self.kwargs['pk']#trae todos los atributos y propiedades que da el cliente
        return  Comentarios.objects.filter(inmuebles=pk) # me trae todos os comentarios que pertenezcan a ese inmueble

class ComentariosDetail(generics.RetrieveUpdateDestroyAPIView): 
    
    queryset = Comentarios. objects. all()
    serializer_class = ComentarioSerializer
    permission_classes=[ComentarioUserOrReadOnly]

     
# metodo 2   
# class ComentarioLis(mixins.ListModelMixin, mixins.CreateModelMixin,generics.GenericAPIView ):
#     queryset = Comentarios. objects. all()
#     serializer_class = ComentarioSerializer
#     def get (self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
    
#     def post (self, request,*args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class ComentariosDetail(mixins.RetrieveModelMixin, generics.GenericAPIView):
#     queryset = Comentarios. objects. all()
#     serializer_class = ComentarioSerializer
    
#     def get (self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
    
    
#I//////////////////////////////////////////////////////////   
class EdificacionListAv(APIView):
    def get(self, request):
        edificaciones=Edificacion.objects.all()
        serializer=EdificacionSerializer(edificaciones, many=True)
        return Response(serializer.data)
    def post(self, request):
        deserializer=EdificacionSerializer(data=request.data)
        if deserializer.is_valid():
            deserializer.save()
            return Response(deserializer.data)
        else:
             return Response(deserializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EdificacionDetalleAv(APIView):
    def get(self, request,pk):
        try:
            edificacion=Edificacion.objects.get(pk=pk)
        except Edificacion.DoesNotExist:
            return Response(('Error el inmueble no existe'), status=status.HTTP_404_NOT_FOUND)
        serializer=EdificacionSerializer(edificacion)
        return Response(serializer.data)
        
    def put(self, request,pk):
        try:
            edificacion=Edificacion.objects.get(pk=pk)
        except Edificacion.DoesNotExist:
            return Response(('Error el inmueble no existe'), status=status.HTTP_404_NOT_FOUND)
        deserializer=EdificacionSerializer(edificacion, data=request.data)
        if deserializer.is_valid():
            deserializer.save()
            return Response(deserializer.data)
        else:
             return Response(deserializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request,pk):
        try:
            edificacion=Edificacion.objects.get(pk=pk)
        except Edificacion.DoesNotExist:
            return Response(('Error el inmueble no existe'), status=status.HTTP_404_NOT_FOUND)
        edificacion.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
 
 #E///////////////////////////////////////   
class EmpresaVs(viewsets.ViewSet):
    # permission_classes=[IsAuthenticated]#es un permiso personalizado
    permission_classes=[adminOrReadOnly]
    def list(self,request):
        queryset = Empresa.objects.all()
        serializer= EmpresaSerializer(queryset,many=True)
        return Response(serializer.data)
    
    
    def retrieve(self,request, pk=None ):#empresa por id
        queryset = Empresa.objects.all()
        inmuebleList= get_object_or_404(queryset,pk=pk)
        serializer= EmpresaSerializer(inmuebleList)
        return Response(serializer.data)
    
    def create(self, request):
        serializer=EmpresaSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def update(self,request,pk):
        try:
            empresa=Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response({'error':'Empresa no encontrada'},status=status.HTTP_404_NOT_FOUND)
        serializer=EmpresaSerializer(empresa, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
            
    def destroy(self, request,pk):
        try:
            empresa=Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response({'error':'Empresa no encontrada'},status=status.HTTP_404_NOT_FOUND)
        empresa.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  
# -------Todo lo anterior se puede resumir en--------------------------------

# class EmpresaVS(viewsets.ModelViewSet):
#     queryset = Empresa.objects.all()
#     serializer_class = EmpresaSerializer
    #con esto se implementa todos los metodos(delete-get-post-update)
    
        
    
class EmpresaListAv(APIView):
    def get(self, request):
        empresa=Empresa.objects.all()
        serializer=EmpresaSerializer(empresa, many=True, context={'request':request})
        #el context es necesario para general el link en el serializer
        return Response(serializer.data)
    def post(self, request):
        deserializer=EmpresaSerializer(data=request.data)
        if deserializer.is_valid():
            deserializer.save()
            return Response(deserializer.data)
        else:
             return Response(deserializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EmpresaDetalleAv(APIView):
    def get(self, request,pk):
        try:
            empresa=Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response(('Error la empresa no existe'), status=status.HTTP_404_NOT_FOUND)
        serializer=EmpresaSerializer(empresa)
        return Response(serializer.data)
        
    def put(self, request,pk):
        try:
            empresa=Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response(('Error la Empresa no existe'), status=status.HTTP_404_NOT_FOUND)
        deserializer=EmpresaSerializer(empresa, data=request.data)
        if deserializer.is_valid():
            deserializer.save()
            return Response(deserializer.data)
        else:
             return Response(deserializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        try:
            empresa=Empresa.objects.get(pk=pk)
        except Empresa.DoesNotExist:
            return Response(('Error la empresa no existe'), status=status.HTTP_404_NOT_FOUND)
        empresa.delete()
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