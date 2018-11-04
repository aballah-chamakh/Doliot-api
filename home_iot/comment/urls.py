from django.urls import path
from django.conf.urls import include
from rest_framework import routers
from .views import CommentView,CommentResponseView

router = routers.DefaultRouter()
router.register('comment', CommentView)
router.register('comment-response', CommentResponseView)

urlpatterns = [
    path('', include(router.urls)),

]
