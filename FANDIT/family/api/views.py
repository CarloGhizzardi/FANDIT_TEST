from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import OrderingFilter
from family.models import Family
from family.api.serializers import FamilySerializer

class FamilyApiViewSet(ModelViewSet):
    serializer_class= FamilySerializer
    queryset= Family.objects.all()
    filter_backends= [OrderingFilter]
    ordering= ['name']