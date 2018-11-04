from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from .views import ThingViewSet,DeviceThingViewSet

router = routers.DefaultRouter()
router.register('thing', ThingViewSet)
router.register('device-thing', DeviceThingViewSet)

urlpatterns = [
    path('', include(router.urls)),

]
