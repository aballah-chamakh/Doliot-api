from rest_framework import serializers
from .models import Bulb,Robot,Plant



class BulbSerializer(serializers.ModelSerializer):
    state = serializers.BooleanField(read_only=True)
    on_image = serializers.CharField(source='on_image.url',read_only=True)
    off_image = serializers.CharField(source='off_image.url',read_only=True)


    class Meta :
        model = Bulb
        fields = ('id','url','name','on_image','off_image','state')

class DeviceBulbSerializer(serializers.ModelSerializer):
    state = serializers.BooleanField(read_only=True)
    class Meta :
        model = Bulb
        fields = ('id','url','name','state')

class RobotSerializer(serializers.ModelSerializer):

    image = serializers.CharField(source='image.url',read_only=True)
    class Meta :
        model = Robot
        fields = ('id','name','image','humidity','temperature')

class PlantSerializer(serializers.ModelSerializer):
    image = serializers.CharField(source='image.url',read_only=True)
    class Meta :
        model = Plant
        fields = ('id','name','image','opened','humidity')
