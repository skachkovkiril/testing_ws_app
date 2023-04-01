from thread_ws import Client
import time
from statistics import mean

from utils import color, coloring


class Result:
    def __init__(self, avg_connection_time, avg_send_recv_time, avg_disconnection_time):
        self.avg_connection_time = avg_connection_time
        self.avg_send_recv_time = avg_send_recv_time
        self.avg_disconnection_time = avg_disconnection_time

    def __str__(self):
        return f"{self.avg_connection_time}\t{self.avg_send_recv_time}\t{self.avg_disconnection_time}"


class Testing:
    def __init__(self, count_clients, url = "ws://127.0.0.1:8000/ws/"):
        self.url = url
        self.clients = [Client(self.url) for _ in range(count_clients)]
        self.avg_connection_time = None
        self.avg_send_recv_time = None
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
    
    def __condition_iteration(self):
        all_recv = [client.fm_is_received for client in self.clients]
        return sum(all_recv) < len(self.clients)

    def __preparation_iteration(self):
        for client in self.clients:
            client.fm_is_received = False

    def experiment(self):
        for i, client in enumerate(self.clients):
            coloring(f"Iteration start {i+1}/{len(self.clients)}")
            start = time.time()
            client.iteration()
            while self.__condition_iteration():
                continue
            end = time.time() - start
            client.send_recv_time = end
            coloring(f"Iteration stop - time: {round(end, 6)} sec.\n", b="180")
            self.__preparation_iteration()
        self.avg_send_recv_time = round(mean([i.send_recv_time for i in self.clients]), 6)

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

    def run(self) -> Result:
        self.start()
        self.experiment()
        self.stop()
        return Result(self.avg_connection_time, self.avg_send_recv_time, self.avg_disconnection_time)

    @color()
    def get_average_connection_speed(self):
        print(f"\nAverage connection time: {self.avg_connection_time} sec.\n", end="")
    
    @color()
    def get_average_send_recv_speed(self):
        print(f"\nAverage send and recieve time: {self.avg_send_recv_time} sec.\n", end="")

    @color()
    def get_average_disconnection_speed(self):
        print(f"\nAverage disconnection time: {self.avg_disconnection_time} sec.\n", end="")
