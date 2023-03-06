from rest_framework import serializers
from animal.models import Animal


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model= Animal
        fields= ['common_name', 'scientific_name', 'family_id', 'in_extinction']

class AnimalZooSerializer(serializers.ModelSerializer):
    class Meta:
        model= Animal
        fields=['scientific_name']