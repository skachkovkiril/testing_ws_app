from test_ws import Testing


if __name__=="__main__":
    testing_obj = Testing(count_clients=4)
    testing_obj.start_with_stop_by_symbol()
