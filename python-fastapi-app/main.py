from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from datetime import datetime


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
        # Необходимо в зависимости от типа сообщения предусмотреть кому отправлять
        # fm - first message
        # bc - broadcast
        # rc - response client
        # rs - response server
        # st - status transfer
        match data["payload"]["tp"]:
            case "rc":
                data["payload"]["tp"] = "rs"
            case "fm":
                data["payload"]["tp"] = "bc"
        for connection in self.active_connections:
            if not websocket is connection:
                await connection.send_json(data=data)


manager = ConnectionManager()


@app.websocket("/ws/{uuid}")
async def websocket_endpoint(websocket: WebSocket, uuid: str):
    await manager.connect(websocket)
    try:
        await manager.broadcast(websocket, {"id": uuid, "payload": {"tp": "cn"}})
        while True:
            data = await websocket.receive_json()
            await manager.broadcast(websocket, {"id": uuid, "payload": data})
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(websocket, {"id": uuid, "payload": {"tp": "ex"}})   