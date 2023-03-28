from blacksheep import Application, WebSocket, WebSocketDisconnectError


app = Application()


class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, data: dict):
        for connection in self.active_connections:
            await connection.send_json(data=data)


manager = ConnectionManager()


@app.router.ws("/ws/{uuid}")
async def ws(websocket: WebSocket, uuid: str):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_json()
            await manager.broadcast(data)
    except WebSocketDisconnectError:
        manager.disconnect(websocket)