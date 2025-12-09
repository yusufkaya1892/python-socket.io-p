import socketio

sio = socketio.Client()

@sio.event
def connect():
    print("Client 2 connected to server.")

@sio.on("new_message")
def handle_new_message(data):
    print(">>", data)

sio.connect("http://localhost:5000")

while True:
    msg = input("Client2 Message: ")
    sio.emit("chat_message", {"username": "Hakan", "message": msg})