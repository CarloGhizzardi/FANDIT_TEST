from rest_framework.viewsets import ModelViewSet
from animal.models import Animal
from animal.api.serializers import AnimalSerializer

class AnimalApiViewSet(ModelViewSet):
    serializer_class= AnimalSerializer 
    queryset= Animal.objects.all()
