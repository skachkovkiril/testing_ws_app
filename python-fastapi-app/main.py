from fastapi import FastAPI, WebSocket, WebSocketDisconnect
import datetime


app = FastAPI(title='WebSocket Example')


class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, websocket: WebSocket, data: dict):
        for connection in self.active_connections:
            if not websocket is connection:
                await connection.send_json(data=data)


manager = ConnectionManager()


@app.websocket("/ws/{uuid}")
async def websocket_endpoint(websocket: WebSocket, uuid: str):
    await manager.connect(websocket)
    try:
        await manager.broadcast(websocket, {"id": uuid, "dt": str(datetime.datetime.now())})
        while True:
            data = await websocket.receive_json()
            await manager.broadcast(websocket, {"id": uuid, "dt": str(datetime.datetime.now()), "data": data})
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(websocket, {"test": f"Client #{websocket} disconnected"})   