from test_ws import Testing


if __name__=="__main__":
    testing_obj = Testing(count_clients=int(input("Required number of users: ")))
    testing_obj.start()
    testing_obj.get_average_connection_speed()
    testing_obj.stop_by_symbol()
    testing_obj.get_average_disconnection_speed()
