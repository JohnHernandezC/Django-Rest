from rest_framework.decorators import api_view
from rest_framework.response import Response
from userApp.api.serializers import registrationSerializers
from rest_framework.authtoken.models import Token
from userApp import models
from rest_framework import status

# @api_view(['POST',])
# def registration_view(request):
#     if request.method=='POST':
#         serializer=registrationSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)


@api_view(['POST',])        
def registration_view(request):
    if request.method=='POST':
        serializer=registrationSerializers(data=request.data)
        data={}
        
        if serializer.is_valid():
            account=serializer.save()
            data['response']='El registro del usuario fue exitoso '
            data['username']=account.username
            data['email']=account.email
            token=Token.objects.get(user=account).key
            data['token']=token
            
        else:
            data=serializer.errors
            
        return Response(data)
    
@api_view(['POST',]) 
def logout_view(request):
    if request.method=='POST':
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)