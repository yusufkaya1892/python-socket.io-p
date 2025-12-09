import socketio
from aiohttp import web
import time

sio = socketio.AsyncServer(async_mode="aiohttp")
app = web.Application()
sio.attach(app)

@sio.event
async def zaman(sid):
    return {"server_time": time.time()}

@sio.event
async def connect(sid, environ):
    print("Client connected:", sid)

@sio.event
async def disconnect(sid):
    print("Client disconnected:", sid)

if __name__ == "__main__":
    web.run_app(app, port=5000)
