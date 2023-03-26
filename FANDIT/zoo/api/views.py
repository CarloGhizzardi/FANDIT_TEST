from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response 
from rest_framework.filters import OrderingFilter
from zoo.models import Zoo
from zoo.api.serializers import ZooSerializer, ZooSerializerGet, ZooSerializerPost, ZooSerializerPut
from family.models import Family


class ZooGetView(APIView):


    def get(self, request):
        zoo= Zoo.objects.all()
        serializer= ZooSerializerGet(zoo, many=True )
        filter_backends= [OrderingFilter]
        ordering= ['family_id','animal_id']
        return Response(serializer.data)


   
    def post(self, request):
        serializer = ZooSerializerPost(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk):
        zoo = self.get_object(pk)
        serializer = ZooSerializerPut(zoo, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        def get_object(self, pk):
            try:
              return Zoo.objects.get(pk=pk)
            except Zoo.DoesNotExist:
              raise Http404


    def delete(self, request, pk, format=None):
        try:
            zoo = Zoo.objects.get(pk=pk)
        except Zoo.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        zoo.animals.clear()
        zoo.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ZooView(ModelViewSet):
    pass
    serializer_class= ZooSerializerGet
    queryset= Zoo.objects.all()
    filter_backends= [OrderingFilter]
    ordering= ['animals']


  







        





