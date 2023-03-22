from threading import Thread
import websocket
from uuid import uuid4
import time
from datetime import datetime
from statistics import mean
import json


def coloring(text, r="38", g="05", b="222"):
    return f"\33[{r};{g};{b}m{text}\033[0;0m"


class WSClient(Thread):
    def __init__(self, url="ws://127.0.0.1:8000/ws/"):
        super().__init__()
        self.uuid_client = uuid4()
        self.url = url
        self.start_open = None
        self.start_close = None
        self.time_open = None
        self.time_close = None
        
    
    def run(self):
        def on_message(ws, message):
            print(coloring(f"Client #{self.uuid_client} - {message}", b="113"))

        def on_error(ws, error):
            print(error)

        def on_close(ws, close_status_code, close_msg):
            self.time_close = datetime.now() - self.start_close
            print(f"Client #{self.uuid_client} - disconnection completed at {datetime.now()} ({self.time_close})")

        def on_open(ws):
            self.time_open = datetime.now() - self.start_open
            print(f"Client #{self.uuid_client} - connection completed at {datetime.now()} ({self.time_open})")
        
        websocket.enableTrace(False)
        self.ws = websocket.WebSocketApp(f"{self.url}{self.uuid_client}",
                                         on_open=on_open,
                                         on_message=on_message,
                                         on_error=on_error,
                                         on_close=on_close)
        self.ws.run_forever()
    
    def send_message(self):
        self.ws.send(json.dumps({"test": str(self.uuid_client)}))


class Testing:
    def __init__(self, count_clients):
        self.clients = [WSClient() for _ in range(count_clients)]
    
    def start(self):
        for client in self.clients:
            client.start_open = datetime.now()
            print(f"Client #{client.uuid_client} - connection start at {client.start_open}")
            client.start()
            time.sleep(0.01)
    
    def stop(self):
        for client in self.clients:
            client.start_close = datetime.now()
            print(f"Client #{client.uuid_client} - disconnection start at {client.start_close}")
            client.ws.close()
            time.sleep(0.01)
    
    def stop_by_symbol(self, symbol="exit"):
        while str(input()) != symbol:
            continue
        self.stop()

    def start_with_stop_by_symbol(self, symbol="exit"):
        self.start()
        self.stop_by_symbol(symbol)
    
    def get_average_connection_speed(self):
        print(coloring(f"\nAverage connection time: {round(mean([i.time_open.total_seconds() for i in self.clients]), 4)} sec.\n"))
    
    def get_average_disconnection_speed(self):
        print(coloring(f"\nAverage disconnection time: {round(mean([i.time_close.total_seconds() for i in self.clients]), 4)} sec.\n"))