from channels.consumer import SyncConsumer, AsyncConsumer

class MySyncCalculator(SyncConsumer):
    def websocket_connect(self, event):
        self.send({"type": "websocket.accept"})
        print("Websocket Connected...")

    def websocket_receive(self, event):
        print(f"Message Receive from Websocket {event}")
        try:
            result = eval(event["text"])
        except Exception as e:
            result = "Invalid Expression"
        self.send({"type": "websocket.send", "text": f"From Calc Server : {result}"})

    def websocket_disconnect(self, event):
        print("Websocket Disconnected...")


class MyAsyncCalculator(AsyncConsumer):
    async def websocket_connect(self, event):
        await self.send({"type": "websocket.accept"})
        print("Websocket Connected...")

    async def websocket_receive(self, event):
        print(f"Message Receive from Websocket {event}")
        try:
            result = eval(event["text"])
        except Exception as e:
            result = "Invalid Expression"
        await self.send(
            {"type": "websocket.send", "text": f"From Calc Server : {result}"}
        )

    async def websocket_disconnect(self, event):
        print("Websocket Disconnected...")
