import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from .models import Machine

class MachineConsumer(WebsocketConsumer):
    def connect(self):
        self.machine_name = self.scope['url_route']['kwargs']['machine_name']
        self.room_group_name = f'machine_{self.machine_name}'

        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name,
            self.channel_name
        )

    def receive(self, text_data):
        data = json.loads(text_data)
        
        # Update the machine in the database
        machine = Machine.objects.get(name=self.machine_name)
        machine.status = data.get('status', machine.status)
        machine.program = data.get('program', machine.program)
        machine.counter = data.get('counter', machine.counter)
        machine.save()

        # Broadcast the update to the client
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type': 'machine_update',
                'data': data
            }
        )

    def machine_update(self, event):
        data = event['data']
        self.send(text_data=json.dumps(data))
