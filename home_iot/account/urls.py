from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from .views import UserViewSet,ProfileViewSet,SimpleProfileRetrieveView

router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('profile', ProfileViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('simple-profile/<slug:slug>/',SimpleProfileRetrieveView.as_view())

]
