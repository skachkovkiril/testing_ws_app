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

    async def broadcast(self, websocket: WebSocket, data: str):
        for connection in self.active_connections:
            if not websocket is connection:
                await connection.send_text(data=data)


manager = ConnectionManager()


@app.websocket("/ws/{id}")
async def websocket_endpoint(websocket: WebSocket, id: int):
    await manager.connect(websocket)
    try:
        await manager.broadcast(websocket, f"Пользователь #{id} подключился к чату ({datetime.datetime.now()})")
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(websocket, data)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(websocket, f"Client #{websocket} disconnected")