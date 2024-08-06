from django.urls import path
from .consumers import MachineConsumer

websocket_urlpatterns = [
    path('ws/machine/<str:machine_name>/', MachineConsumer.as_asgi()),
]
