from django.conf.urls import include
from django.urls import path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('user', views.UserViewSet)
router.register('button', views.ButtonViewSet)
router.register('lamp', views.LampViewSet)

urlpatterns = [
    path('api/', include(router.urls)),

]
