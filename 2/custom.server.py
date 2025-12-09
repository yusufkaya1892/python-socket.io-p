import socketio
from aiohttp import web

sio = socketio.AsyncServer(async_mode='aiohttp')
app = web.Application()
sio.attach(app)

@sio.event
async def login(sid, data):
    username = data.get("username")
    level = data.get("level")

    response = f"Hello {username}! Your level is {level}."
    print("[SERVER] Sending:", response)

    await sio.emit("login_response", response, to=sid)

@sio.event
async def connect(sid, environ):
    print("[SERVER] Client connected:", sid)

@sio.event
async def disconnect(sid):
    print("[SERVER] Client disconnected:", sid)


if __name__ == "__main__":
    web.run_app(app, port=5000)
