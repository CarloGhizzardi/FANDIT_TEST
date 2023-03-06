from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from animal.models import Animal
from animal.api.serializers import AnimalSerializer

class AnimalApiViewSet(ModelViewSet):
    serializer_class= AnimalSerializer 
    queryset= Animal.objects.all()
    filter_backends= [OrderingFilter]
    ordering= ['common_name']
