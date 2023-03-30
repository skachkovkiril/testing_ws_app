import { createServer } from 'http';
import { parse } from 'url';
import WebSocket, { WebSocketServer } from 'ws';

const server = createServer();
const wss = new WebSocketServer({ noServer: true });


wss.on('connection', function connection(ws, request, client) {
  console.log("open");
  ws.on("message", (message) => {
    wss.clients.forEach(client=>{
        if(client.readyState === WebSocket.OPEN)
            client.send(`${message}`);
    })
  });

  ws.on("close", (event) => {
    console.log("close");
  });
});


server.on('upgrade', function upgrade(request, socket, head) {
    const { pathname } = parse(request.url);
    if (pathname.includes("/ws/")) {
      wss.handleUpgrade(request, socket, head, function done(ws) {
        wss.emit('connection', ws, request);
      });
    } else {
      socket.destroy();
    }
  });
  
  server.listen(8000);
