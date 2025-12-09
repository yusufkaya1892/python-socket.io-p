import socketio
import asyncio

sio = socketio.AsyncClient()

@sio.on("login_response")
async def on_login_response(data):
    print("[CLIENT] Server says:", data)

@sio.event
async def connect():
    print("[CLIENT] Connected to server!")

async def main():
    await sio.connect("http://localhost:5000")

    await sio.emit("login", {
        "username": "Ali",
        "level": 5
    })

    await asyncio.sleep(2)  #bekle
    await sio.disconnect()

asyncio.run(main())
