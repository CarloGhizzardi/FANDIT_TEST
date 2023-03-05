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
    ordering= ['zoo_id', 'family_id', 'animal_id']

   # def get(self, queryset):
    #    for zoo in zoo_id:

    



   # def list(self, request):
        #serializer= ZooSerializer(Zoo.objects.all(), many=True)

    #    serializer2= AnimalRegistrationSerializer(AnimalRegistration.objects.filter().order_by('family_id'), many=True)
    #    return Response(status= status.HTTP_200_OK, data=serializer2.data)



        
        
