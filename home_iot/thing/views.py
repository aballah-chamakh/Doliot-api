from django.shortcuts import render
from rest_framework import viewsets,status,generics
from .serializers import ThingSerializer,DeviceThingSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Thing 
from django.shortcuts import get_object_or_404
from Shared.permissions import IsOwnerOrReadOnly


class ThingViewSet(viewsets.ModelViewSet):
    serializer_class = ThingSerializer
    queryset = Thing.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)
    @action(methods=['PUT'],detail=True)
    def switch_on(self,request,pk):
        thing_obj = self.get_object()
        thing_obj.state = True
        thing_obj.save()
        serializer = ThingSerializer(thing_obj,many=False,context={'request':request})
        return Response({'response':serializer.data},status=status.HTTP_200_OK)
    @action(methods=['PUT'],detail=True)
    def switch_off(self,request,pk):
        thing_obj = self.get_object()
        thing_obj.state = False
        thing_obj.save()
        serializer = ThingSerializer(thing_obj,many=False,context={'request':request})
        return Response({'response':serializer.data},status=status.HTTP_200_OK)
    def perform_create(self,serializer):
        profile_obj = self.request.user.profile
        serializer.save(profile=profile_obj)


# this view is designed to be resquested from the thing which's devices like Raspberry pi or arduino ...
class DeviceThingViewSet(viewsets.ModelViewSet):
    serializer_class = DeviceThingSerializer
    queryset = Thing.objects.all()
    permission_classes = (IsOwnerOrReadOnly,)
    @action(methods=['PUT'],detail=True)
    def switch_on(self,request,pk):
        thing_obj = self.get_object()
        thing_obj.state = True
        thing_obj.save()
        serializer = ThingSerializer(thing_obj,many=False,context={'request':request})
        return Response({'response':serializer.data},status=status.HTTP_200_OK)
    @action(methods=['PUT'],detail=True)
    def switch_off(self,request,pk):
        thing_obj = self.get_object()
        thing_obj.state = False
        thing_obj.save()
        serializer = ThingSerializer(thing_obj,many=False,context={'request':request})
        return Response({'response':serializer.data},status=status.HTTP_200_OK)
    def perform_create(self,serializer):
        profile_obj = self.request.user.profile
        serializer.save(profile=profile_obj)
