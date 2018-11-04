from rest_framework import serializers
from .models import Comment,CommentResponse
from account.UserSerializer import SimpleUserSerializer



class CommentSerializer(serializers.HyperlinkedModelSerializer):
    username  = serializers.CharField(source='owner.username',read_only=True)
    image     = serializers.ImageField(source='owner.profile.image',read_only=True)
    responses = serializers.SerializerMethodField('get_all_responses',read_only=True)
    likes     = serializers.SerializerMethodField('get_all_likes',read_only=True)
    user_id = serializers.IntegerField(source='owner.id',read_only=True)
    profile_slug = serializers.SlugField(source='owner.profile.slug',read_only=True)

    class Meta :
        model = Comment
        fields = ('id','owner','user_id','profile_slug','username','image','content','responses','likes')
    def get_all_responses(self,obj):
        comment_obj = obj
        responses = comment_obj.commentresponse_set.all()
        serializer = CommentResponseSerializer(responses,many=True,context={'request':self.context['request']})
        return serializer.data
    def get_all_likes(self,obj):
        comment_obj = obj
        likes = comment_obj.likes.all()
        serializer = SimpleUserSerializer(likes,many=True,context={'request':self.context['request']})
        return serializer.data

class CommentResponseSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.CharField(source='owner.username',read_only=True)
    image = serializers.ImageField(source='owner.profile.image',read_only=True)
    likes = serializers.SerializerMethodField('get_all_like',read_only=True)
    user_id = serializers.IntegerField(source='owner.id',read_only=True)
    profile_slug = serializers.SlugField(source='owner.profile.slug',read_only=True)
    class Meta :
        model = CommentResponse
        fields = ('id','profile_slug','comment','owner','user_id','content','username','image','likes')
    def get_all_like(self,obj):
        commentResponse_obj = obj
        likes = commentResponse_obj.likes.all()
        serializers = SimpleUserSerializer(likes,many=True,context={'request':self.context['request']})
        return serializers.data
