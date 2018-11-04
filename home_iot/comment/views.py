from .serializers import CommentSerializer,CommentResponseSerializer
from .models import Comment,CommentResponse
from documentation.models import Documentation
from account.UserSerializer import SimpleUserSerializer
from rest_framework import viewsets,status
from rest_framework.decorators import action
from rest_framework.response import Response
from Shared.permissions import IsOwnerOrReadOnly


class CommentResponseView(viewsets.ModelViewSet):
    serializer_class = CommentResponseSerializer
    queryset = CommentResponse.objects.all()
    permissons_classes = [IsOwnerOrReadOnly]

    def perform_create(self,serializer):
        comment_id = self.request.GET.get('comment_id')
        comment_obj = Comment.objects.get(id = comment_id)
        user_obj = None
        if self.request.user.is_authenticated :
            user_obj = self.request.user
            print(user_obj.username)
        serializer.save(comment=comment_obj,owner=user_obj)
    @action(methods=['POST'],detail=True)
    def update_res_comment(self,request,pk):
        res_comment_obj = self.get_object()
        content = request.data.get('content')
        res_comment_obj.content = content
        res_comment_obj.save()
        return Response({'msg':'successfully the response comment updated'},status=status.HTTP_200_OK)

    @action(methods=['PUT'],detail=True)
    def toogle_like(self,request,pk):
        res_comment_obj  = CommentResponse.objects.get(id=pk)
        user_obj = request.user
        if res_comment_obj.likes.all().count() == 0 :
            if user_obj  :
                    res_comment_obj.likes.add(user_obj)
                    serializer = SimpleUserSerializer(res_comment_obj.likes.all(),many=True,context={'request':self.request})
                    return Response({'likes':serializer.data},status=status.HTTP_200_OK)
        else :
            if user_obj  :
                action = 'add'
                if user_obj in res_comment_obj.likes.all() :
                    action = 'remove'
                if action == 'add' :
                    res_comment_obj.likes.add(user_obj)
                    serializer = SimpleUserSerializer(res_comment_obj.likes.all(),many=True,context={'request':self.request})
                    print(user_obj.username+' like added')
                    return Response({'likes':serializer.data},status=status.HTTP_200_OK)
                elif action == 'remove':
                    res_comment_obj.likes.remove(user_obj)
                    serializer = SimpleUserSerializer(res_comment_obj.likes.all(),many=True,context={'request':self.request})
                    print(user_obj.username+' like removed')
                    return Response({'likes':serializer.data},status=status.HTTP_200_OK)
            else :
                return Response({'msg':'anonymos user'},status=status.HTTP_400_BAD_REQUEST)

class CommentView(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    queryset = Comment.objects.all()
    permissons_classes = [IsOwnerOrReadOnly]
    @action(methods=['POST'],detail=True)
    def update_comment(self,request,pk):
        comment_obj = self.get_object()
        content = request.data.get('content')
        comment_obj.content = content
        comment_obj.save()
        return Response({'msg':'successfully the comment updated'},status=status.HTTP_200_OK)
    @action(methods=['PUT'],detail=True)
    def toogle_like(self,request,pk):
        comment_obj  = Comment.objects.get(id=pk)
        user_obj = request.user
        if comment_obj.likes.all().count() == 0 :
            if user_obj  :
                    comment_obj.likes.add(user_obj)
                    serializer = SimpleUserSerializer(comment_obj.likes.all(),many=True,context={'request':self.request})
                    return Response({'likes':serializer.data},status=status.HTTP_200_OK)
        else :
            if user_obj  :
                action = 'add'
                if user_obj in comment_obj.likes.all() :
                    action = 'remove'
                if action == 'add' :
                    comment_obj.likes.add(user_obj)
                    serializer = SimpleUserSerializer(comment_obj.likes.all(),many=True,context={'request':self.request})
                    print(user_obj.username+' like added')
                    return Response({'likes':serializer.data},status=status.HTTP_200_OK)
                elif action == 'remove':
                    comment_obj.likes.remove(user_obj)
                    serializer = SimpleUserSerializer(comment_obj.likes.all(),many=True,context={'request':self.request})
                    print(user_obj.username+' like removed')
                    return Response({'likes':serializer.data},status=status.HTTP_200_OK)
            else :
                return Response({'msg':'anonymos user'},status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self,serializer):
        doc_id = self.request.GET.get('doc_id')
        print(doc_id)
        doc_obj = None
        if doc_id :
            doc_obj = Documentation.objects.get(id = doc_id)
        owner = None
        if self.request.user.is_authenticated :
            owner = self.request.user
        serializer.save(owner=owner,documentation=doc_obj)
