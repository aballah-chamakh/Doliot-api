from django.db import models
from account.models import User
from documentation.models import Documentation


class Comment(models.Model):
    owner = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    documentation = models.ForeignKey(Documentation,on_delete=models.CASCADE,blank=True,null=True)
    content = models.TextField()
    likes   = models.ManyToManyField(User,blank=True,related_name='comment_likes')

    def __str__(self):
        owner = 'none'
        if (self.owner is not None):
            owner = self.owner.username
        return 'comment owned by '+owner




class CommentResponse(models.Model):
    comment  = models.ForeignKey(Comment,on_delete=models.CASCADE,blank=True,null=True)
    owner    = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    content  = models.TextField()
    likes   = models.ManyToManyField(User,blank=True,related_name='res_comment_likes')

    def __str__(self):
        owner = 'none'
        if (self.owner is not None):
            owner = self.owner.username
        return 'comment response owned by '+owner
