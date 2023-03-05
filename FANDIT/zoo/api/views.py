from rest_framework import status
#from rest_framework.views import APIView
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response 
from zoo.models import Zoo, AnimalRegistration
from zoo.api.serializers import ZooSerializer, AnimalRegistrationSerializer



class ZooViewSet(ViewSet):
    def list(self, request):
        serializer= ZooSerializer(Zoo.objects.all(), many=True)
        #animals= AnimalRegistrationSerializer(AnimalRegistration.objects.order_by('family_id'))
        return Response(status= status.HTTP_200_OK, data= serializer.data)

        
        
