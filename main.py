from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from typing import List, Dict

app = FastAPI()

class ConnectionManager():
    def __init__(self):
        self.Rooms: Dict[str, List[WebSocket]] = {}

    async def connect(self, socket: WebSocket, room: str):
        await socket.accept()
        if room not in self.Rooms:
            self.Rooms[room] = []
        self.Rooms[room].append(socket)

    def disconnect(self, socket: WebSocket, room: str):
        self.Rooms[room].remove(socket)

    async def send_broadcast(self, message: str, room: str):
        for ppl in self.Rooms[room]:
            await ppl.send_text(message)

ConnectionNum1 = ConnectionManager()

@app.websocket("/ws/{room}/{user}")
async def websocket_endpoint(socket: WebSocket, room: str, user: str):
    await ConnectionNum1.connect(socket, room)
    await ConnectionNum1.send_broadcast(f'USER "{user}" has connected to room "{room}"', room)
    
    try:
        while True:
            data = await socket.receive_text()
           
            await ConnectionNum1.send_broadcast(f'{user}: {data}', room)
            
    except WebSocketDisconnect:
        ConnectionNum1.disconnect(socket, room)
        await ConnectionNum1.send_broadcast(f'USER "{user}" has left the room "{room}"', room)