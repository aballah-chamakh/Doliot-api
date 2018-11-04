from django.contrib import admin
from .models import Comment,CommentResponse
# Register your models here.
admin.site.register(Comment)
admin.site.register(CommentResponse)
