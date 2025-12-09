from flask import Flask
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config["SECRET_KEY"] = "secret!"
socketio = SocketIO(app)


@socketio.on("chat_message")
def handle_chat_message(data):
    username = data.get("username", "Unknown")
    message = data.get("message", "")
    broadcast_msg = f"{username} says: {message}"

    emit("new_message", broadcast_msg, broadcast=True)


if __name__ == "__main__":
    print("Server is running on http://localhost:5000")
    socketio.run(app, host="0.0.0.0", port=5000)

