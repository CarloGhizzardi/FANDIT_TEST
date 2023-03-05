from rest_framework.routers import DefaultRouter
from zoo.api.views import ZooViewSet

router_zoo= DefaultRouter()

router_zoo.register(prefix= 'zoo', basename= 'zoo', viewset=ZooViewSet)