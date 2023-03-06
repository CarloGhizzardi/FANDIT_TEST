from rest_framework import serializers
from zoo.models import Zoo, AnimalRegistration
from animal.api.serializers import AnimalSerializer
from animal.models import Animal





class ZooSerializer(serializers.ModelSerializer):
   # animal_id = serializers.IntegerField()
    #quantity = serializers.IntegerField()
    
    class Meta:
        model = Zoo
        fields = ['name', 'city', 'country', 'surface', 'budget']

class ZooSerializerGet(serializers.ModelSerializer):
     
    class Meta:
        model = Zoo
        fields = ['name', 'city', 'country', 'surface', 'budget']      


class AnimalRegistrationSerializer(serializers.ModelSerializer):
    zoo_id= ZooSerializerGet()
    animal_id= AnimalSerializer()
    class Meta:      
        model= AnimalRegistration
        fields= 'zoo_id','animal_id', 'quantity'


        


        