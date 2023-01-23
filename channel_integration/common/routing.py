from django.urls import path
from channel_integration.apps.calc import consumers as calc
from channel_integration.apps.simple import consumers as simple
websocket_urlpatterns = [
    path("ws/sc/", simple.MySyncConsumer.as_asgi()),
    path("ws/ac/", simple.MyAsyncConsumer.as_asgi()),
    path("ws/sc/calc/", calc.MySyncCalculator.as_asgi()),
    path("ws/ac/calc/", calc.MySyncCalculator.as_asgi()),
]
