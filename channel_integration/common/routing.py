from django.urls import path
from channel_integration.apps.calc import consumers

websocket_urlpatterns = [
    path("ws/sc/", consumers.MySyncConsumer.as_asgi()),
    path("ws/ac/", consumers.MyAsyncConsumer.as_asgi()),
    path("ws/sc/calc/", consumers.MySyncCalculator.as_asgi()),
    path("ws/ac/calc/", consumers.MySyncCalculator.as_asgi()),
]
