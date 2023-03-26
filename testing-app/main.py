from testing_app import Testing


if __name__=="__main__":
    app = Testing(count_clients=int(input("Enter the number of clients: ")))
    app.start()
    app.experiment()
    app.stop()
    
    app.get_average_connection_speed()
    app.get_average_send_recv_speed()
    app.get_average_disconnection_speed()
