from rest_framework import serializers
from .models import Documentation
from account.UserSerializer import SimpleUserSerializer
from comment.models import Comment
from comment.serializers import CommentSerializer


class DocumentationSerializer(serializers.HyperlinkedModelSerializer):
    comments = serializers.SerializerMethodField('get_related_comment',read_only=True)
    likes = serializers.SerializerMethodField('get_all_likes',read_only=True)
    class Meta :
        model = Documentation
        fields = ('id','slug','image','title','breif','description','likes','comments')
    def get_related_comment(self,obj):
        comments = Comment.objects.all().filter(documentation=obj).order_by('-id')
        serializer = CommentSerializer(comments,many=True,context={'request': self.context['request']})
        return serializer.data
    def get_all_likes(self,obj):
        likes = obj.likes.all()
        serializer = SimpleUserSerializer(likes,many=True,context={'request': self.context['request']})
        return serializer.data

class SimpleDocumentationSerializer(serializers.HyperlinkedModelSerializer):
    class Meta :
        model = Documentation
        fields = ('id','slug','image','title','breif')
