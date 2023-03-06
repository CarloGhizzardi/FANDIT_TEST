from rest_framework import serializers
from zoo.models import Zoo 
from animal.api.serializers import AnimalSerializer, AnimalZooSerializer
from animal.models import Animal





class ZooSerializer(serializers.ModelSerializer):
       
    class Meta:
        model = Zoo
        fields = ['name', 'city', 'country', 'surface', 'budget']

class AnimalsSerializers(serializers.RelatedField):
    def to_representation(self, value):
        return value.scientific_name


class ZooSerializerGet(serializers.ModelSerializer):
    animals= AnimalsSerializers(read_only=True, many=True) 
    class Meta:
        model = Zoo
        fields = ['name', 'city', 'country', 'surface', 'budget', 'animals']    




class ZooSerializerPost(serializers.ModelSerializer):
    animals= AnimalZooSerializer()

    class Meta:
        model= Zoo
        fields= ['name', 'city', 'country', 'surface', 'budget', 'animals']
        


        