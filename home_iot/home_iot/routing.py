from django.conf.urls import url
from django.urls import path
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
from thing.consumers import RobotConsumer,BulbConsumer
from .tokenmiddlware import TokenAuthMiddlewareStack
application = ProtocolTypeRouter({

    "websocket": TokenAuthMiddlewareStack(
        URLRouter([
            path('ws/robot/<int:pk>/', RobotConsumer),
            path('ws/bulb/<int:pk>/',BulbConsumer)
        ])
    ),

})
