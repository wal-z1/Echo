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
        if room in self.Rooms and socket in self.Rooms[room]:
            self.Rooms[room].remove(socket)

    async def send_broadcast(self, message: str, room: str):
        if room not in self.Rooms:
            return
            
        # Iterate over a copy of the list so we can remove items safely if needed
        # and catch errors if a socket is dead
        for ppl in self.Rooms[room][:]: 
            try:
                await ppl.send_text(message)
            except Exception:
                # If sending fails remove it from the room
                # and continue sending to the others
                if ppl in self.Rooms[room]:
                    self.Rooms[room].remove(ppl)

ConnectionNum1 = ConnectionManager()

@app.websocket("/ws/{room}/{user}")
async def websocket_endpoint(socket: WebSocket, room: str, user: str):
    await ConnectionNum1.connect(socket, room)
    
    try:
        # Broadcast connection message
        await ConnectionNum1.send_broadcast(f'USER "{user}" has connected to room "{room}"', room)
        
        while True:
            data = await socket.receive_text()
            await ConnectionNum1.send_broadcast(f'{user}: {data}', room)
            
    except WebSocketDisconnect:
        ConnectionNum1.disconnect(socket, room)
        await ConnectionNum1.send_broadcast(f'USER "{user}" has left the room "{room}"', room)
    except Exception as e:
        # Catch other errors 
        print(f"Error: {e}")
        ConnectionNum1.disconnect(socket, room)