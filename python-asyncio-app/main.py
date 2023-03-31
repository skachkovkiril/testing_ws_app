import asyncio
import websockets

class ConnectionManager:
    def __init__(self):
        self.active_connections = []

    async def connect(self, websocket):
        self.active_connections.append(websocket)

    def disconnect(self, websocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, data: dict):
        websockets.broadcast(self.active_connections, data)


manager = ConnectionManager()

async def handler(websocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.recv()
            await manager.broadcast(data)
    except:
        manager.disconnect(websocket)


async def main():
    async with websockets.serve(handler, "0.0.0.0", 8000):
        await asyncio.Future()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass