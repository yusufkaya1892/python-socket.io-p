import socketio
import asyncio

sio = socketio.AsyncClient()

@sio.event
async def connect():
    print("Connected to server")

@sio.event
async def disconnect():
    print("Disconnected from server")

async def main():
    await sio.connect("http://localhost:5000")

    while True:
        data = await sio.call("zaman")
        print("Server time:", data["server_time"])
        await asyncio.sleep(1)

asyncio.run(main())
