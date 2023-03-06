from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response 
from rest_framework.filters import OrderingFilter
from zoo.models import Zoo
from zoo.api.serializers import ZooSerializer






#class ZooView(ModelViewSet):
#    pass
#    serializer_class= AnimalRegistrationSerializer
#    queryset= AnimalRegistration.objects.all()
#    filter_backends= [OrderingFilter]
#    ordering= ['zoo_id', 'animal_id']




class ZooRegisterView(APIView):
    def post(self, request, format=None):
        serializer = ZooSerializer(data=request.data)
        if serializer.is_valid():
            zoo = serializer.save()
            animal_id = request.data.get('animal_id')
            quantity = request.data.get('quantity')
            zoo_registration = AnimalRegistration.objects.create(zoo_id=zoo, animal_id=animal_id, quantity=quantity)
            return Response({'status': 'success'})
        return Response(serializer.errors, status=400)



#    def post(self, request):
#        serializer= AnimalRegistrationSerializer(data=request.data)
#
#        if serializer.is_valid(raise_exception=True):
#            serializer.save()
#            return Response(serializer.data)

#        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)


class ZooShowView(APIView):
    def get(self, request):
        registros= AnimalRegistration.objects.all()
        serializer= AnimalRegistrationSerializer(registros, many=True)
        filter_backends= [OrderingFilter]
        ordering= ['zoo_id', 'animal_id']
        return Response(serializer.data)




        





