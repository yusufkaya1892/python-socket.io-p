import socketio
from aiohttp import web

baglanti = socketio.AsyncServer()
uygulama = web.Application()
baglanti.attach(uygulama)

@baglanti.event
async def mesaj_oda(sid, veri):
    oda = veri.get("oda")
    mesaj = veri.get("mesaj")
    await baglanti.emit("mesaj_yayin", {"mesaj": mesaj}, room=oda)

@baglanti.event
async def giris_oda(sid, veri):
    oda = veri.get("oda")
    await baglanti.enter_room(sid, oda)
    await baglanti.emit("mesaj_yayin", {"mesaj": f"{sid} {oda} odasına katıldı"}, room=oda)

@baglanti.event
async def connect(sid, environ):
    print(f"İstemci bağlandı: {sid}")

@baglanti.event
async def disconnect(sid):
    print(f"İstemci ayrıldı: {sid}")

if __name__ == '__main__':
    web.run_app(uygulama)