from rest_framework import serializers
from zoo.models import Zoo, AnimalRegistration
from animal.api.serializers import AnimalSerializer
from family.api.serializers import FamilySerializer

class ZooSerializer(serializers.ModelSerializer):
    class Meta:
        model= Zoo
        fields= ['name', 'city', 'country', 'surface', 'budget']


class AnimalRegistrationSerializer(serializers.ModelSerializer):

#muestre los datos del zoo y los animales su cantidad y ordenados por categoria

    zoo_id= ZooSerializer()
    animal_id= AnimalSerializer('scientific_name')
    family_id= FamilySerializer()


    #species=serializers.SerializerMethodField()

    class Meta:      
        model= AnimalRegistration
        fields= ['zoo_id', 'animal_id', 'family_id']

    







    #def to_representation(self, instance):
       # response = super().to_representation(instance)
        #response['animal_id', 'family_id'] = AlbumSerializer(instance.album).data
        #return response    

    