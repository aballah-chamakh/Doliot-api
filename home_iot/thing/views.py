from django.shortcuts import render
from rest_framework import viewsets,status,generics,permissions
from .serializers import BulbSerializer,DeviceBulbSerializer,RobotSerializer,PlantSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Bulb,Robot,Plant
from django.shortcuts import get_object_or_404
from Shared.permissions import IsOwnerOrReadOnly


class BulbViewSet(viewsets.ModelViewSet):
    serializer_class = BulbSerializer
    queryset = Bulb.objects.all()
    permission_classes = [IsOwnerOrReadOnly,]
    @action(methods=['PUT'],detail=True)
    def switch_on(self,request,pk):
        bulb_obj = self.get_object()
        bulb_obj.state = True
        bulb_obj.save()
        serializer = BulbSerializer(bulb_obj,many=False,context={'request':request})
        return Response({'response':serializer.data},status=status.HTTP_200_OK)
    @action(methods=['PUT'],detail=True)
    def switch_off(self,request,pk):
        bulb_obj = self.get_object()
        bulb_obj.state = False
        bulb_obj.save()
        serializer = BulbSerializer(bulb_obj,many=False,context={'request':request})
        return Response({'response':serializer.data},status=status.HTTP_200_OK)
    def perform_create(self,serializer):
        profile_obj = self.request.user.profile
        serializer.save(profile=profile_obj)


# this view is designed to be resquested from the thing which's devices like Raspberry pi or arduino ...
class DeviceBulbViewSet(viewsets.ModelViewSet):
    serializer_class = DeviceBulbSerializer
    queryset = Bulb.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)
    @action(methods=['PUT'],detail=True)
    def switch_on(self,request,pk):
        bulb_obj = self.get_object()
        bulb_obj.state = True
        bulb_obj.save()
        serializer = ThingSerializer(bulb_obj,many=False,context={'request':request})
        return Response({'response':serializer.data},status=status.HTTP_200_OK)
    @action(methods=['PUT'],detail=True)
    def switch_off(self,request,pk):
        bulb_obj = self.get_object()
        bulb_obj.state = False
        bulb_obj.save()
        serializer = ThingSerializer(bulb_obj,many=False,context={'request':request})
        return Response({'response':serializer.data},status=status.HTTP_200_OK)
    def perform_create(self,serializer):
        profile_obj = self.request.user.profile
        serializer.save(profile=profile_obj)

class RobotViewSet(viewsets.ModelViewSet) :
    queryset = Robot.objects.all()
    serializer_class = RobotSerializer

    def perform_create(self,serializer):
        profile_obj = self.request.user.profile
        serializer.save(profile=profile_obj)

class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer


    def perform_create(self,serializer):
        profile_obj = self.request.user.profile
        serializer.save(profile=profile_obj)
