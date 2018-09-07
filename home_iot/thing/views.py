from django.shortcuts import render
from rest_framework import viewsets,status
from .serializers import *
from .permissions import IsOwnerOrReadOnly
from rest_framework.decorators import action
from rest_framework.response import Response

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permisson_classes = (IsOwnerOrReadOnly,)

class LampViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = Lamp.objects.all()
    permisson_classes = (IsOwnerOrReadOnly,)
    @action(methods=['POST'],detail=True)
    def toogle_lamp(self,requets,pk):
        lamp_obj = self.get_object()
        lamp_obj.state = not lamp_obj.state
        lamp_obj.save()
        return Response({'response':'button toogled successfully'},status=status.HTTP_200_OK)

class ButtonViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = Button.objects.all()
    permisson_classes = (IsOwnerOrReadOnly,)
    @action(methods=['POST'],detail=True)
    def toogle_button(self,requets,pk):
        button_obj = self.get_object()
        button_obj.state = not button_obj.state
        button_obj.save()
        return Response({'response':'button toogled successfully'},status=status.HTTP_200_OK)
