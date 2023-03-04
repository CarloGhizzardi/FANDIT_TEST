from rest_framework import serializers
from zoo.models import Zoo, AnimalRegistration

class ZooSerializer(serializers.ModelSerializer):
    model= Zoo
    fields= ['name', 'city', 'countrys', 'surface', 'budget']


class AnimalRegistrationSerializer(serializers.ModelSerializer):
    model= AnimalRegistration
    fields= ['zoo_id', 'animal_id', 'family_id']

    