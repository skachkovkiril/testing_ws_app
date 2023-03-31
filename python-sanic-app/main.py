from sanic import Sanic
from sanic import Request, Websocket
import json

app = Sanic("WebSocketExample")


class ConnectionManager:
    def __init__(self):
        self.active_connections: list = []

    async def connect(self, websocket):
        self.active_connections.append(websocket)

    def disconnect(self, websocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, data: dict):
        for connection in self.active_connections:
            await connection.send(json.dumps(data))


manager = ConnectionManager()


@app.websocket("/ws/<uuid>")
async def feed(request: Request, ws: Websocket, uuid: str):
    await manager.connect(ws)
    try:
        while True:
            data = json.loads(await ws.recv())
            await manager.broadcast(data)
    except:
        manager.disconnect(ws)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)