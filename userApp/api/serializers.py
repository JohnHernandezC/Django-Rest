from rest_framework import serializers
from django.contrib.auth.models import User

class registrationSerializers(serializers.ModelSerializer):
    password2 = serializers.CharField(style={'input_type': 'password'},write_only=True)
    
    class Meta:
        model=User
        fields=['username','email','password','password2']
        extra_Kwargs={'password':{'write_only':True}
                      }
        
    def save(self):
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        
        if password != password2:
            raise  serializers.validationError({'error':'el password de confirmacion no coincide'})
        
        if User.objects.filter(email=self.validated_data['email']).exists():
            raise serializers.validationError({'error':'el email del usuario ya existe'})
        account=User(email=self.validated_data['email'],username=self.validated_data['username'])
        account.set_password(password)
        account.save()
        return account