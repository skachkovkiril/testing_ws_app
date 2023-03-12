from threading import Thread
import websocket
from uuid import uuid4
import time


class WSClient(Thread):
    def __init__(self, url="ws://127.0.0.1:8000/ws/"):
        super().__init__()
        self.uuid_client = uuid4()
        self.url = url
        
    
    def run(self):
        def on_message(ws, message):
            print(f"Client #{self.uuid_client} - {message}")

        def on_error(ws, error):
            print(error)

        def on_close(ws, close_status_code, close_msg):
            print(f"Client #{self.uuid_client} - disconnected")

        def on_open(ws):
            print(f"Client #{self.uuid_client} - connected")
        
        websocket.enableTrace(False)
        self.ws = websocket.WebSocketApp(f"{self.url}{self.uuid_client}",
                                         on_open=on_open,
                                         on_message=on_message,
                                         on_error=on_error,
                                         on_close=on_close)
        self.ws.run_forever()


class Testing:
    def __init__(self, count_clients):
        self.clients = [WSClient() for _ in range(count_clients)]
    
    def start(self):
        for client in self.clients:
            client.start()
            time.sleep(0.1)
    
    def stop(self):
        for client in self.clients:
            client.ws.close()
            time.sleep(0.1)
    
    def stop_by_symbol(self, symbol="0"):
        while str(input()) != symbol:
            continue
        self.stop()

    def start_with_stop_by_symbol(self, symbol="0"):
        self.start()
        self.stop_by_symbol(symbol=symbol)