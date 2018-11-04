from rest_framework import serializers
from .models import Thing



class ThingSerializer(serializers.HyperlinkedModelSerializer):
    state = serializers.BooleanField(read_only=True)
    class Meta :
        model = Thing
        fields = ('id','url','name','on_image','off_image','state')

class DeviceThingSerializer(serializers.HyperlinkedModelSerializer):
    state = serializers.BooleanField(read_only=True)
    class Meta :
        model = Thing
        fields = ('id','url','name','state')
