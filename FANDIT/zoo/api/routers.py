from rest_framework.routers import DefaultRouter
from zoo.api.views import ZooView

router_zoos= DefaultRouter()
router_zoos.register(prefix= 'zoo', basename='zoo', viewset=ZooView)
