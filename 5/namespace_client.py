import socketio
import asyncio

sio = socketio.AsyncClient()

@sio.event(namespace="/chat")
async def connect():
    print("[CHAT] Connected to chat namespace")

@sio.on("chat_message", namespace="/chat")
async def on_chat_message(data):
    print("[CHAT] Received:", data)

@sio.event(namespace="/status")
async def connect():
    print("[STATUS] Connected to status namespace")

async def main():
    await sio.connect("http://localhost:5000", namespaces=["/chat", "/status"])

    await sio.emit("chat_message", " Monaco Galatasaray 1.5 üst ", namespace="/chat")

    response = await sio.call("health_check", "ping", namespace="/status")
    print("[STATUS] Server returned:", response)

    await asyncio.sleep(2)
    await sio.disconnect()

asyncio.run(main())
