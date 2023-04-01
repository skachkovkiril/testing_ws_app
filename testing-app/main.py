from testing_app import Testing


if __name__=="__main__":
    host = str(input("Host: "))
    apps = {
        "python-fastapi-app": 8001,
        "python-sanic-app": 8002,
        "python-starlette-app": 8003,
        "python-blacksheep-app": 8004,
        "python-tornado-app": 8005,
        "python-asyncio-app": 8006,
        "js-express-app": 8007,
        "js-websocket-app": 8008,
    }
    count_clients=int(input("Enter the number of clients: "))
    results = {}
    for app in apps:
        application = Testing(count_clients=count_clients, url=f"ws://{host}:{apps[app]}/ws/")
        results[app] = application.run()
    
    for result in results:
        print(f"{result}\t {results[result]}")
