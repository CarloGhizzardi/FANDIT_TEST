from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response 
from rest_framework.filters import OrderingFilter
from zoo.models import Zoo, AnimalRegistration
from zoo.api.serializers import ZooSerializer, AnimalRegistrationSerializer, ZooRegisterSerializer



class ZooView(ModelViewSet):
    pass
 #   serializer_class= AnimalRegistrationSerializer
  #  queryset= AnimalRegistration.objects.all()
   # filter_backends= [OrderingFilter]
    #ordering= ['zoo_id', 'animal_id']




class ZooRegisterView(APIView):
    def post(self, request):
        serializer= ZooRegisterSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        serializer= AnimalRegistrationSerializer()
        #filter_backends= [OrderingFilter]
        #ordering= ['zoo_id', 'animal_id']
        return Response(serializer.data)




        





