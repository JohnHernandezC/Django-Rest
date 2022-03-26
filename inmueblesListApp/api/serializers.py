from rest_framework import serializers

from inmueblesListApp.models import Inmueble


def columLongitud(value):#validaciones dentro del objeto serializador
    if len(value)<2:
        raise serializers.ValidationError('el valor es demasiado corto')
    #esto se agrega dentro del objeto a validar en este caso 
    
    
    
class InmuebleSerializer(serializers.Serializer):
    id=serializers.IntegerField(read_only=True)
    direccion=serializers.CharField(validators=[columLongitud])
    pais=serializers.CharField(validators=[columLongitud])
    descripcion=serializers.CharField()
    imagen=serializers.CharField()
    active=serializers.BooleanField()
    
    def create(self,validate_data):
        return Inmueble.objects.create(**validate_data)
    
    def update(self,instance,validated_data):
        instance.direccion = validated_data.get('direccion', instance.direccion)
        instance.pais = validated_data.get('pais', instance.pais)
        instance.descripcion = validated_data.get('descripcion', instance.descripcion)
        instance.imagen = validated_data.get('imagen', instance.imagen)
        instance.active = validated_data.get('active', instance.active)
        instance.save()
        return instance
    def validate(self,data):# esta es una funcion predefinida dentro de Django la estamos modificando
        if data['direccion'] == data['pais']:
            raise serializers.ValidationError('la direccion y el pais deben ser diferentes')
        else:
            return data 
    def validate_imagen(self,data):#validate_imagen pude ser tambien validate_pais o_descripcion dependiendo de lo que se necesite
        if len(data)>2:
            raise serializers.ValidationError('el url de la imagen es muy corto')
        else:
            return data 