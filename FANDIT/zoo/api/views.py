from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response 
from rest_framework.filters import OrderingFilter
from zoo.models import Zoo, AnimalRegistration
from zoo.api.serializers import ZooSerializer, AnimalRegistrationSerializer



class ZooViewSet(ModelViewSet):
    serializer_class= AnimalRegistrationSerializer
    queryset= AnimalRegistration.objects.all()
    filter_backends= [OrderingFilter]
    ordering= ['zoo_id', 'animal_id']

  #  def list(sel, queryset):
 #       for zoo in zoo_id:
   #         registro= AnimalRegistration.objects.count(zoo_id= zoo)


        
        
