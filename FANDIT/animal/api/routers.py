from rest_framework.routers import DefaultRouter
from animal.api.views import AnimalApiViewSet

router_animal= DefaultRouter()

router_animal.register(prefix= 'animal', basename= 'animal', viewset=AnimalApiViewSet)
