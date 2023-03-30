import json

import tornado.web
import tornado.ioloop
import tornado.websocket


class WebSocket(tornado.websocket.WebSocketHandler):
    def open(self, slug):
        self.application.webSocketsPool.append(self)

    def on_message(self, message):
        for _, value in enumerate(self.application.webSocketsPool):
            value.ws_connection.write_message(message)

    def on_close(self, message=None):
        for key, _ in enumerate(self.application.webSocketsPool):
            del self.application.webSocketsPool[key]

class Application(tornado.web.Application):
    def __init__(self):
        self.webSocketsPool = []
        handlers = (
            (r'/ws/([^/]+)', WebSocket),
        )
        tornado.web.Application.__init__(self, handlers)

application = Application()


if __name__ == '__main__':
    application.listen(8000)
    tornado.ioloop.IOLoop.instance().start()