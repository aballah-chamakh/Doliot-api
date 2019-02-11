from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from .views import BulbViewSet,DeviceBulbViewSet,RobotViewSet,PlantViewSet

router = routers.DefaultRouter()
router.register('bulb', BulbViewSet)
router.register('robot', RobotViewSet)
router.register('plant', PlantViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
