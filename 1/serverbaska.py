import socket
import threading


HEADER = 64
PORT = 5000
SERVER = socket.gethostbyname(socket.gethostname())
##print(SERVER)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ADDR = (SERVER, PORT)
FORMAT = 'utf-8'
DISCONNECT_alert = "!Disconnected"

server.bind(ADDR)

def handle_client(conn, addr):
    print(f"[New connection] {addr} connected")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)

            if msg == DISCONNECT_alert:
                connected = False

            print(f"[{addr}] {msg}") 

    conn.close()

def starting():
    server.listen()
    print(F"[Listening server] is on {SERVER}")
    while True:
        conn, addr = server.accept()
        thread = threading.Thread(target= handle_client, args=(conn, addr))
        thread.start()
        print(f"[Active connection] {threading.active_count() - 1}")


print(f"[Starting the server]...")
starting()

