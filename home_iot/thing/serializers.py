from rest_framework import serializers
from .models import *


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(style={'input_type':'password'},write_only=True,required=True)
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True,required=True)

    class Meta :
        model = User
        fields =('username','email','password','password2')
    def validate(self,data):
        pw1 = data.get('password')
        pw2 = data.pop('password2')
        if pw1 != pw2 :
            raise serializers.ValidationError('Passwords should match')
        return data
    def create(self,validated_data):
        username = validated_data.get('username')
        email = validated_data.get('email')
        password = validated_data.get('password')
        user_obj = User(username=username,email=email)
        user_obj.set_password(password)
        user_obj.save()
        return user_obj

class LampSerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = Lamp
        fields = ('owner','name','state')

class ButtonSerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = Button
        fields = ('owner','name','state')
