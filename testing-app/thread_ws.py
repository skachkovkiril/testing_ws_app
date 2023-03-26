from threading import Thread
import websocket
from uuid import uuid4
import time
import json

from utils import coloring


class Client(Thread):
    def __init__(self, url="ws://127.0.0.1:8000/ws/"):
        super().__init__()
        self.uuid_client = uuid4()
        self.url = url
        self.is_connect = False
        self.connection_time = None
        self.disconnection_time = None
    
    def run(self):
        def on_message(ws, message):
            coloring(f"Client #{self.uuid_client} - {message}", b="68")

        def on_error(ws, error):
            coloring(error, b="196")

        def on_open(ws):
            self.is_connect = True

        def on_close(ws, close_status_code, close_msg):
            self.is_connect = False
        
        websocket.enableTrace(False)
        self.ws = websocket.WebSocketApp(f"{self.url}{self.uuid_client}",
                                         on_open=on_open,
                                         on_message=on_message,
                                         on_error=on_error,
                                         on_close=on_close)
        self.ws.run_forever()
    
    def iteration(self):
        print(f"Client #{self.uuid_client} - send first message")

    def stop(self):
        self.ws.close()