var express = require("express");
var expressWs = require("express-ws");
var expressWs = expressWs(express());
var app = expressWs.app;

app.use(express.static("public"));

var aWss = expressWs.getWss("/");

app.ws("/ws/:uuid", function (ws, req) {
  console.log("open");
  ws.on("message", (msg) => {
    aWss.clients.forEach((client) => {
      client.send(msg);
    });
  });
  ws.on("close", () => {
    console.log("close");
  });
});

app.listen(8000);
