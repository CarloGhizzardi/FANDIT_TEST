from rest_framework import serializers
from zoo.models import Zoo, AnimalRegistration
from animal.api.serializers import AnimalSerializer
from family.api.serializers import FamilySerializer

class ZooSerializer(serializers.ModelSerializer):
    class Meta:
        model= Zoo
        fields= ['name', 'city', 'country', 'surface', 'budget']
      


class AnimalRegistrationSerializer(serializers.ModelSerializer):
    zoo_id= ZooSerializer()
    animal_id= AnimalSerializer()
    class Meta:      
        model= AnimalRegistration
        fields= ['zoo_id','animal_id','quantity']


class ZooRegisterSerializer(serializers.ModelSerializer):
    zoo_id= ZooSerializer()
    animal_id= AnimalSerializer()

    class Meta:      
        model= AnimalRegistration
        fields= ['zoo_id', 'animal_id', 'quantity']

        