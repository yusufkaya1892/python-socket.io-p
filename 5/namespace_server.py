import socketio
from aiohttp import web

class namespace_chati(socketio.AsyncNamespace):
    def on_connect(self, sid, environ):
        print(f"[CHAT] Client connected: {sid}")

    async def on_chat_message(self, sid, data):
        print(f"[CHAT] Received message: {data}")
        await self.emit("chat_message", f"Echo: {data}")

class namespace_status(socketio.AsyncNamespace):
    def on_connect(self, sid, environ):
        print(f"[STATUS] Client connected: {sid}")

    async def on_health_check(self, sid, data):
        print(f"[STATUS] Health check received: {data}")
        return "ok"


sio = socketio.AsyncServer(async_mode='aiohttp')
app = web.Application()
sio.attach(app)

sio.register_namespace(namespace_chati('/chat'))
sio.register_namespace(namespace_status('/status'))

if __name__ == '__main__':
    web.run_app(app, port=5000)
