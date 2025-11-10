from socketio import Client
import json

sio = Client()

@sio.event
def connect():
    print("Connecté au serveur Socket.IO")

@sio.event
def disconnect():
    print("Déconnecté du serveur")

@sio.on('error')
def on_error(data):
    print("Error:", data)

@sio.on('response')
def on_response(data):
    print("Response:", data)


sio.connect('http://localhost:5000')
log = {
    "time_agent": "2025-09-30T12:00:00",
    "host": "greed-island",
    "ip": "10.10.10.10",
    "layout": "fr",
    "input": "whoami[ENTER]"
}
sio.emit('log', log)


sio.wait()
sio.disconnect()
