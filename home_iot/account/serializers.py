from rest_framework import serializers
from .models import Profile
from thing.models import Thing
from thing.serializers import ThingSerializer



class ProfileSerializer(serializers.HyperlinkedModelSerializer) :
    things = serializers.SerializerMethodField('get_all_things',read_only=True)
    username = serializers.CharField(source='user.username',read_only=True)
    class Meta :
        model  = Profile
        fields = ('id','slug','user','username','image','summary','things')
    def get_all_things(self,obj):
        things = Thing.objects.all().filter(profile=obj)
        serializer = ThingSerializer(things,many=True,context={'request':self.context['request']})
        return serializer.data


class SimpleProfileSerializer(serializers.HyperlinkedModelSerializer) :
    username = serializers.CharField(source='user.username',read_only=True)
    class Meta :
        model  = Profile
        fields = ('id','slug','username','image')
