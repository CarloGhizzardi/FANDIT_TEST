from rest_framework import serializers
from zoo.models import Zoo 
from animal.api.serializers import AnimalSerializer
from animal.models import Animal





class ZooSerializer(serializers.ModelSerializer):
       
    class Meta:
        model = Zoo
        fields = ['name', 'city', 'country', 'surface', 'budget']

class ZooSerializerGet(serializers.ModelSerializer):
     
    class Meta:
        model = Zoo
        fields = ['name', 'city', 'country', 'surface', 'budget']      





        


        