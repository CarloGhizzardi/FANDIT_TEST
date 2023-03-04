from rest_framework.routers import DefaultRouter
from family.api.views import FamilyApiViewSet

router_family= DefaultRouter()

router_family.register(prefix= 'family', basename= 'family', viewset=FamilyApiViewSet)
