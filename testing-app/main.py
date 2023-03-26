from testing_app import Testing


if __name__=="__main__":
    app = Testing(count_clients=3)
    app.start()
    app.get_average_connection_speed()
    # app.experiment()
    app.stop()
    app.get_average_disconnection_speed()
