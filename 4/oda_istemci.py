import socketio

istemci = socketio.Client()

@istemci.event
def connect():
    print("Sunucuya bağlanıldı")
    istemci.emit("giris_oda", {"oda": "chatAlpha"})

@istemci.event
def mesaj_yayin(veri):
    print("Mesaj geldi:", veri["mesaj"])

@istemci.event
def disconnect():
    print("Sunucudan ayrıldın")

istemci.connect("http://localhost:8080")
istemci.emit("mesaj_oda", {"oda": "chatAlpha", "mesaj": "Merhaba Chat Alpha!"})
istemci.wait()