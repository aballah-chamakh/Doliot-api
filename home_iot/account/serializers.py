from rest_framework import serializers
from .models import Profile
from thing.models import Bulb,Robot,Plant
from thing.serializers import BulbSerializer,RobotSerializer,PlantSerializer




class ProfileSerializer(serializers.ModelSerializer) :
    bulbs = serializers.SerializerMethodField('get_all_bulbs',read_only=True)
    plants = serializers.SerializerMethodField('get_all_plants')
    robots = serializers.SerializerMethodField('get_all_robots')
    username = serializers.CharField(source='user.username',read_only=True)
    image = serializers.CharField(source='image.url',read_only=True)
    class Meta :
        model  = Profile
        fields = ('id','slug','user','username','image','summary','bulbs','robots','plants')

    def get_all_bulbs(self,obj):
        things = Bulb.objects.filter(profile=obj)
        serializer = BulbSerializer(things,many=True,context={'request':self.context['request']})
        return serializer.data

    def get_all_robots(self,obj) :
        robots = Robot.objects.filter(profile=obj)
        serializer = RobotSerializer(robots,many=True,context={'request':self.context['request']})
        return serializer.data

    def get_all_plants(self,obj) :
        plants = Plant.objects.filter(profile=obj)
        serializer = PlantSerializer(plants,many=True,context={'request':self.context['request']})
        return serializer.data

class SimpleProfileSerializer(serializers.ModelSerializer) :
    username = serializers.CharField(source='user.username',read_only=True)
    image = serializers.CharField(source='image.url',read_only=True)

    class Meta :
        model  = Profile
        fields = ('id','slug','username','image')
