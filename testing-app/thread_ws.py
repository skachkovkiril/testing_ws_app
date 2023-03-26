from threading import Thread
import websocket
from uuid import uuid4
from datetime import datetime
import json

from utils import coloring


class Client(Thread):
    def __init__(self, url="ws://127.0.0.1:8000/ws/"):
        super().__init__()
        self.uuid_client = uuid4()
        self.url = url
        self.is_connect = False
        self.connection_time = None
        self.send_recv_time = None
        self.disconnection_time = None
        self.fm_is_received = False
    
    def run(self):
        def on_message(ws, message):
            self.fm_is_received = True

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
        coloring(f"Client #{self.uuid_client} - send first message", b="68")
        self.ws.send(json.dumps({
            "id": str(self.uuid_client),
            "dt": str(datetime.now()),
            "tp": "fm"
        }))

    def stop(self):
        self.ws.close()