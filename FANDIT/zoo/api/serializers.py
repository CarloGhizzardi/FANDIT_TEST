from rest_framework import serializers
from zoo.models import Zoo, AnimalRegistration

class ZooSerializer(serializers.ModelSerializer):
    class Meta:
        model= Zoo
        fields= ['name', 'city', 'country', 'surface', 'budget']


class AnimalRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model= AnimalRegistration
        fields= ['zoo_id', 'animal_id', 'family_id']

    