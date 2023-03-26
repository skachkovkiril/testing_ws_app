from thread_ws import Client
import time
from statistics import mean

from utils import color, coloring


class Testing:
    def __init__(self, count_clients):
        self.url = "ws://127.0.0.1:8000/ws/"
        self.clients = [Client(self.url) for _ in range(count_clients)]
        self.avg_connection_time = None
        self.avg_disconnection_time = None

    def start(self):
        for client in self.clients:
            start = time.time()
            coloring(f"Client #{client.uuid_client} - connection start", b="113")
            client.start()
            while not client.is_connect:
                continue
            end = time.time() - start
            client.connection_time = end
            coloring(f"Client #{client.uuid_client} - connection completed", b="65")
        self.avg_connection_time = round(mean([i.connection_time for i in self.clients]), 6)
    
    def experiment(self):
        for client in self.clients:
            client.iteration()
        

    def stop(self):
        for client in self.clients:
            start = time.time()
            coloring(f"Client #{client.uuid_client} - disconnection start", b="113")
            client.stop()
            while client.is_alive() and client.is_connect:
                continue
            end = time.time() - start
            client.disconnection_time = end
            coloring(f"Client #{client.uuid_client} - disconnection completed", b="65")
        self.avg_disconnection_time = round(mean([i.disconnection_time for i in self.clients]), 6)

    @color()
    def get_average_connection_speed(self):
        print(f"\nAverage connection time: {self.avg_connection_time} sec.\n", end="")
    
    @color()
    def get_average_disconnection_speed(self):
        print(f"\nAverage disconnection time: {self.avg_disconnection_time} sec.\n", end="")
