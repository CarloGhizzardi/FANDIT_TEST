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

        def create(self, validated_data):
            animals_data= validated_data.pop('animal')
            zoo= Zoo.objects.create(**validated_data)
            for animal_data in animals_data:
                Animals.objects.create(zoo=zoo, **animal_data)
            return zoo
        



class ZooSerializerPut(serializers.ModelSerializer):
    class Meta:
        model = Zoo
        fields = ['id', 'name', 'city', 'country', 'surface', 'budget', 'animals']
        read_only_fields = ['id', 'animals']

    def create(self, validated_data):
        animals_data = validated_data.pop('animals')
        zoo = Zoo.objects.create(**validated_data)
        for animal_data in animals_data:
            zoo.animals.add(animal_data)
        return zoo

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.city = validated_data.get('city', instance.city)
        instance.country = validated_data.get('country', instance.country)
        instance.surface = validated_data.get('surface', instance.surface)
        instance.budget = validated_data.get('budget', instance.budget)


